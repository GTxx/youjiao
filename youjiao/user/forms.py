from flask_security.forms import RegisterForm, NewPasswordFormMixin, PasswordConfirmFormMixin
import inspect
from flask_security.forms import RegisterFormMixin
from wtforms import StringField, PasswordField, Field
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.validators import Regexp
from flask_security.forms import UniqueEmailFormMixin
from flask import current_app
from werkzeug.local import LocalProxy
from .models import User, Captcha
from flask import after_this_request


def unique_user_name(form, field):
    if User.query.filter_by(name=field.data).first() is not None:
        raise ValidationError('name already exists')

def unique_email(form, field):
    if User.query.filter_by(email=field.data).first() is not None:
        raise ValidationError('email already exists')


class RegisterForm(Form):
    name_validators = [
        DataRequired(), unique_user_name,
        Regexp(r'[\w.+-]', message='Enter a valid name'),
        Length(min=4, max=30)
    ]
    password_validators = [DataRequired(), Length(min=6, max=30)]
    password_confirm_validators = password_validators + [EqualTo('password', 'retry password mismatch')]
    email_validators = [DataRequired(), unique_email, Email('email not valid')]

    name = StringField(u'name', validators=name_validators)
    email = StringField(u'email', validators=email_validators)
    password = PasswordField(u'password', validators=password_validators)
    password_confirm = PasswordField(u'password_confirm', validators=password_confirm_validators)
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

    def to_dict(self):
        def is_field_and_user_attr(member):
            return isinstance(member, Field) and \
                hasattr(User, member.name)

        fields = inspect.getmembers(self, is_field_and_user_attr)
        return dict((key, value.data) for key, value in fields)
