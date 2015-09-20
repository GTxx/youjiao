from flask import Blueprint, render_template, request, redirect, session, current_app
from flask.views import MethodView
from .decorators import anonymous_user_required
from flask_principal import identity_changed, AnonymousIdentity
from .forms import RegisterForm, UserProfileForm, ModifyPasswordForm
from youjiao.extensions import limiter
from .models import Captcha, User, UserProfile
from flask_login import login_user, login_required, current_user
import json

user_bp = Blueprint("user_view", __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
@anonymous_user_required
def register():
    # TODO: use method view to refactor
    if request.method == 'POST':
        print(request.json)
        print(request.form)
        form = RegisterForm(request.form)
        #import ipdb; ipdb.set_trace()
        if form.validate_on_submit():
            # TODO: register complete and jump to user profile or index page
            data = form.to_dict()
            from .utils import encrypt_password
            data['password'] = encrypt_password(data['password'])
            # TODO: add transaction
            user = User(**data)
            user = user.save()
            user_profile = UserProfile(user_id=user.id)
            user_profile.save()
            login_user(user, force=True)
            return redirect('/')
        # else:
        #     import ipdb; ipdb.set_trace()
    elif request.method == 'GET':
        form = RegisterForm()
        form.hidden_tag()
    # generate new captcha
    # captcha = Captcha.generate()
    return render_template('security/register_user.html',
                           register_user_form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
@anonymous_user_required
def login():
    from .forms import LoginForm
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate_on_submit():
            user = form.user
            # TODO: support token auth in @loging_required, refer to flask_security @auth_required
            # login_required
            login_user(user, force=True)
            from flask_principal import identity_changed, Identity
            from flask import current_app
            identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(user.id))
            if 'admin' in user.roles_name:
                return redirect('/admin/')
            elif 'editor' in user.roles_name:
                return redirect('/admin/')
            else:
                return redirect('/')
    elif request.method == 'GET':
        form = LoginForm()
    return render_template('security/login.html', form=form)


@user_bp.route('/logout')
def logout():
    from flask_login import logout_user, current_user
    if current_user.is_authenticated():
        logout_user()

        # Remove session keys set by Flask-Principal
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        # Tell Flask-Principal the user is anonymous
        identity_changed.send(current_app._get_current_object(),
                              identity=AnonymousIdentity())
    return redirect(request.args.get('next', None) or '/')


@user_bp.route('/refresh_captcha/')
@limiter.limit('1 per second')
def refresh_captcha():
    captcha_key = session.get('captcha_key')
    if not captcha_key:
        return json.dumps({'error': 'not captcha key, refresh page'})
    captcha = Captcha.query.filter_by(key=captcha_key).first()
    if not captcha:
        return json.dumps({'error': 'not captcha key, refresh page'})

    captcha = Captcha.query.filter_by(key=captcha_key).first_or_404()

    captcha = Captcha.generate(captcha.key)

    return json.dumps({'captcha_key': captcha.key, 'url': captcha.img_url})


@user_bp.route('/user/info/profile')
@login_required
def user_info():
    return render_template('user/info.html')


@user_bp.route('/user/favor')
@login_required
def user_favor():
    from youjiao.user_util.models import Favor
    from youjiao.book.models import Book
    from sqlalchemy import and_
    favor_book = Favor.query.filter(and_(Favor.user_id==current_user.id, Favor.obj_type=='book')).with_entities(Favor.obj_id).all()
    book_list = Book.query.filter(Book.id.in_(favor_book))
    return render_template('user/user_favor.html', book_list=book_list )



class UserProfileView(MethodView):
    """ user profile edit """
    methods = ['GET', 'POST']
    decorators = [login_required, ]

    def get(self):
        profile = current_user.profile
        form = UserProfileForm(obj=profile)
        # import ipdb; ipdb.set_trace()
        return render_template('user/profile.html', form=form)

    def post(self):
        # import ipdb; ipdb.set_trace()
        form = UserProfileForm(formdata=request.form)
        if form.validate_on_submit():
            data = form.data
            user_profile = current_user.profile
            form.populate_obj(user_profile)
            user_profile.save()
        return render_template('user/profile.html', form=form)


class UserPasswordModifyView(MethodView):
    methods = ['GET', 'POST']
    decorators = [login_required, ]

    def get(self):
        form = ModifyPasswordForm()

        return render_template('user/modify_password.html', form=form)

    def post(self):
        form = ModifyPasswordForm(formdata=request.form)
        if form.validate_on_submit():
            current_user.set_password(form.data['password'])
            return render_template('user/modify_password.html', modify_success=True, form=form)
        return render_template('user/modify_password.html', form=form)




user_bp.add_url_rule('/user/profile', view_func=UserProfileView.as_view('user_profile'), endpoint='user_profile')
user_bp.add_url_rule('/user/modify_password', view_func=UserPasswordModifyView.as_view('modify_password'), endpoint='modify_password')
