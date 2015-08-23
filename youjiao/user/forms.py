from flask_security.forms import RegisterForm, NewPasswordFormMixin, PasswordConfirmFormMixin
from flask_security.forms import RegisterFormMixin
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.validators import Regexp
from flask_security.forms import UniqueEmailFormMixin
from flask import current_app
from werkzeug.local import LocalProxy
from .models import User, Captcha
from flask import after_this_request


def unique_user_name(form, field):
    if User.query.filter_by(id=field.data).first() is not None:
        raise ValidationError('name already exists')


class RegisterForm(Form, NewPasswordFormMixin, PasswordConfirmFormMixin,
                   UniqueEmailFormMixin, RegisterFormMixin):
    name_validator_list = [
        DataRequired(), unique_user_name,
        Regexp(r'[\w.+-]', message='Enter a valid name'),
        Length(min=5, max=30)
    ]
    name = StringField(u'name', name_validator_list=name_validator_list)
    captcha_key = StringField(u'captcha_key', validators=[Length(min=64, max=64)])
    captcha_content = StringField(u'captcha_content', validators=[Length(min=4, max=4)])

    def validate(self):
        captcha_key = self.captcha_key.data.strip()
        captcha_content = self.captcha_content.data.strip()

        captcha = Captcha.query.filter_by(key=captcha_key, content=captcha_content.upper()).first()

        # always delete captcha
        @after_this_request
        def delete_captcha(response):
            if captcha:
                captcha.delete()
            return response

        if not captcha:
            self.captcha_content.errors += ('captcha error', )
            return False
        if not super(RegisterForm, self).validate():
            return False

        return True

