from flask_security.forms import RegisterForm, NewPasswordFormMixin, PasswordConfirmFormMixin
from flask_security.forms import RegisterFormMixin
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import Form, RecaptchaField
from wtforms import ValidationError
from flask_security.forms import UniqueEmailFormMixin
from flask import current_app
from werkzeug.local import LocalProxy
from .models import User, Captcha


def unique_user_name(form, field):
    if User.query.filter_by(id=field.data).first() is not None:
        raise ValidationError('name already exists')


class RegisterForm(Form, NewPasswordFormMixin, PasswordConfirmFormMixin,
                   UniqueEmailFormMixin, RegisterFormMixin):
    name = StringField(u'name', validators=[DataRequired(), unique_user_name])
    captcha_key = StringField(u'captcha', validators=[Length(min=64, max=64)])
    captcha_content = StringField(u'captcha_key', validators=[Length(min=4, max=4)])

    def validate(self):
        if not super(RegisterForm, self).validate():
            return False

        captcha_key = self.captcha_key.data.strip()
        captcha_content = self.captcha_content.data.strip()

        captcha = Captcha.query.filter_by(key=captcha_key, content=captcha_content.upper()).first()
        if not captcha:
            self.captcha_content.errors.append('captcha error')
            return False
        captcha.delete()
        return True

