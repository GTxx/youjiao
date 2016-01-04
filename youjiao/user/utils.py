import string
import random
import hashlib
import hmac
import base64
from flask import current_app, request
from flask_login import current_user
from flask_principal import UserNeed, RoleNeed
from werkzeug.local import LocalProxy
from datetime import date
from youjiao.extensions import jwt
from flask_security.utils import encrypt_password


def generate_random_string_64():
    return ''.join(random.choice(string.letters+string.digits) for i in range(64))


def generate_random_string_4():
    return ''.join(random.choice(string.ascii_uppercase+string.digits) for i in range(4))


def generate_random_number_4():
    return ''.join(random.choice(string.digits) for i in range(4))


from passlib.context import CryptContext
def _get_password_context():
    return CryptContext(
        schemes=[
            'bcrypt',
            'des_crypt',
            'pbkdf2_sha256',
            'pbkdf2_sha512',
            'sha256_crypt',
            'sha512_crypt',
            # And always last one...
            'plaintext'
        ],
        default=current_app.config['PASSWORD_HASH'])


password_context = LocalProxy(lambda: _get_password_context())
def encrypt_password(password):
    signed = get_hmac(password).decode('ascii')
    return password_context.encrypt(signed)


def verify_password(password, hashed_password):
    signed = get_hmac(password).decode('ascii')
    return password_context.verify(signed, hashed_password)


def get_hmac(password):

    from flask_security.utils import encode_string
    """Returns a Base64 encoded HMAC+SHA512 of the password signed with the salt specified
    by ``PASSWORD_SALT``.

    :param password: The password to sign
    """
    salt = current_app.config.get('PASSWORD_SALT')

    if salt is None:
        raise RuntimeError(
            'The configuration value `PASSWORD_SALT` must '
            'not be None when the value of `PASSWORD_HASH` is '
            'set to "%s"' % salt)

    h = hmac.new(encode_string(salt), encode_string(password), hashlib.sha512)
    return base64.b64encode(h.digest())


def load_user(userid):
    """ flask_login used to load user"""
    from .models import User
    return User.query.filter_by(id=userid).first()


@jwt.identity_handler
def identity(payload):
    # print(payload)
    # import ipdb; ipdb.set_trace()
    from .models import User
    user_id = payload.get('identity')
    return User.query.filter(User.id==user_id).first()
    # return None


@jwt.authentication_handler
def authenticate(username, password):
    from youjiao.user.models import User
    user = User.verify(username, password)
    return user if user else None


def _on_identity_loaded(sender, identity):
    """ flask_principal used to load user"""
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))

    # provide vip need
    if hasattr(current_user, 'vips'):
        from youjiao.user.models import User, VIP
        from youjiao.extensions import db
        e = VIP.query.filter(VIP.user_id==current_user.id,
                             VIP.end>date.today()).exists()
        if db.session.query(e).scalar():
            identity.provides.add(RoleNeed('vip'))
    if hasattr(current_user, 'roles'):
        if ('admin' in current_user.roles_name) or ('editor' in current_user.roles_name):
            identity.provides.add(RoleNeed('vip'))

    identity.user = current_user


def jwt_auth_method():
    from flask_jwt import _jwt_required, current_identity
    from youjiao.extensions import login_manager
    try:
        _jwt_required(current_app.config['JWT_DEFAULT_REALM'])

        # load user to flask_login
        login_manager.reload_user(user=current_identity)
        return True
    except Exception as e:
        print(e)
    else:
        return False


def handle_unauthorized_response():
    from flask_jwt import _jwt_required
    if request.mimetype == 'application/json':
        _jwt_required(current_app.config['JWT_DEFAULT_REALM'])
    else:
        return current_app.login_manager.unauthorized()


def auth_required(auth_methods=['session', 'jwt']):
    """
    inspired by flask security, now support flask_login and flask_jwt
    Decorator that protects enpoints through multiple mechanisms
    Example::

        @app.route('/dashboard')
        @auth_required(auth_methods=['jwt', 'session'])
        def dashboard():
            return 'Dashboard'

    :param auth_methods: Specified mechanisms.
    """
    from functools import partial, wraps
    login_mechanisms = {
        'session': lambda: current_user.is_authenticated,
        'jwt': jwt_auth_method
    }

    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            # import ipdb; ipdb.set_trace()
            mechanisms = [login_mechanisms.get(method) for method in auth_methods]
            for mechanism in mechanisms:
                if mechanism and mechanism():
                    return fn(*args, **kwargs)
            return handle_unauthorized_response()
        return decorated_view
    return wrapper