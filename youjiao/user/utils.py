import string
import random
from flask import current_app
from werkzeug.local import LocalProxy


def generate_random_string_64():
    return ''.join(random.choice(string.letters+string.digits) for i in range(64))


def generate_random_string_4():
    return ''.join(random.choice(string.ascii_uppercase+string.digits) for i in range(4))


def generate_random_number_4():
    return ''.join(random.choice(string.digits) for i in range(4))

from flask_login import login_user, logout_user
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


def get_hmac(password):
    import hashlib
    import hmac
    import base64
    from flask_security.utils import encode_string
    """Returns a Base64 encoded HMAC+SHA512 of the password signed with the salt specified
    by ``SECURITY_PASSWORD_SALT``.

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
    from .models import User
    return User.query.filter_by(id=userid).first()
