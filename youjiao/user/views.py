from flask import Blueprint, render_template, request, redirect
from flask_security.decorators import anonymous_user_required
from .forms import RegisterForm
from youjiao.extensions import db
from .models import Captcha, User
import json

user_bp = Blueprint("user_view", __name__)
from flask_security.views import register
#
# @anonymous_user_required
# def register():
#     """View function which handles a registration request."""
#
#     if _security.confirmable or request.json:
#         form_class = _security.confirm_register_form
#     else:
#         form_class = _security.register_form
#
#     if request.json:
#         form_data = MultiDict(request.json)
#     else:
#         form_data = request.form
#
#     form = form_class(form_data)
#
#     if form.validate_on_submit():
#         user = register_user(**form.to_dict())
#         form.user = user
#
#         if not _security.confirmable or _security.login_without_confirmation:
#             after_this_request(_commit)
#             login_user(user)
#
#         if not request.json:
#             if 'next' in form:
#                 redirect_url = get_post_register_redirect(form.next.data)
#             else:
#                 redirect_url = get_post_register_redirect()
#
#             return redirect(redirect_url)
#         return _render_json(form, include_auth_token=True)
#
#     if request.json:
#         return _render_json(form)
#
#     return _security.render_template(config_value('REGISTER_USER_TEMPLATE'),
#                                      register_user_form=form,
#                                      **_ctx('register'))
#
from flask_security.utils import user_registered
from flask_login import login_user
@user_bp.route('/register', methods=['GET', 'POST'])
@anonymous_user_required
def register():

    if request.method == 'POST':
        print(request.json)
        print(request.form)
        form = RegisterForm(request.form)
        import ipdb; ipdb.set_trace()
        if form.validate_on_submit():
            # TODO: register complete and jump to user profile or index page
            data = form.to_dict()
            from .utils import encrypt_password
            data['password'] = encrypt_password(data['password'])
            user = User(**data)
            user = user.save()
            login_user(user, force=True)
            return redirect('/')
        # else:
        #     import ipdb; ipdb.set_trace()
    elif request.method == 'GET':
        form = RegisterForm()
    # generate new captcha
    captcha = Captcha.generate()
    return render_template('security/register_user.html',
                           register_user_form=form, captcha_key=captcha.key,
                           captcha_url=captcha.img_url)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    pass


@user_bp.route('/logout')
def logout():
    pass


@user_bp.route('/refresh_captcha/<captcha_key>')
def refresh_captcha(captcha_key):
    captcha = Captcha.query.filter_by(key=captcha_key).first_or_404()

    # delete old one and create a new captcha
    db.session.delete(captcha)
    db.session.commit()

    captcha = Captcha()
    db.session.add(captcha)
    db.session.commit()
    return json.dumps({'captcha_key': captcha.key, 'url': captcha.key})


@user_bp.route('/login')
def login():
    return 'test'
