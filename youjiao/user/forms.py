# -*- coding: utf-8 -*-
from flask_security.forms import RegisterForm
import inspect
from flask import flash, request, session
from wtforms import HiddenField
from wtforms import StringField, PasswordField, Field
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.validators import Regexp
import hashlib
import os
from wtforms.widgets.core import HTMLString
from .models import User, Captcha


def unique_user_name(form, field):
    if User.query.filter_by(name=field.data).first() is not None:
        raise ValidationError('name already exists')


def unique_email(form, field):
    if User.query.filter_by(email=field.data).first() is not None:
        raise ValidationError('email already exists')


def check_captcha(captcha_content):
    captcha_key = session.get('captcha_key')
    if not captcha_key:
        raise ValidationError('have no captcha key in session')
    captcha = Captcha.query.filter_by(key=captcha_key).first()
    if not captcha:
        raise ValidationError('captcha error')
    if captcha.content != captcha_content:
        raise ValidationError('captcha error')


def captcha_validator(form, field):
    return check_captcha(field.data)


class CaptcharWidget(object):
    def __call__(self, field, **kwargs):
        # generate captcha

        if 'captcha_key' not in session:
            session['captcha_key'] = hashlib.sha1(os.urandom(64)).hexdigest()
        captcha = Captcha.generate(str(session['captcha_key']))
        return HTMLString('<img src=%s>' % captcha.img_url)

class CaptchaField(Field):
    '''captcha在CaptchaWidget中生成，
    captcha_key在session中，每个用户有唯一的captcha_key，通过这个captcha_key
    做captcha匹配
    '''
    def __init__(self, validators=None, **kwargs):
        validators = validators or [captcha_validator, ]
        super(CaptchaField, self).__init__(validators=validators, **kwargs)

    widget = CaptcharWidget()


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
    captcha = CaptchaField()

    def validate(self):
        captcha = self.captcha.data
        try:
            if not captcha:
                raise ValidationError('captcha is required')
            check_captcha(captcha)
        except ValidationError as e:
            self.captcha.errors += (str(e), )
            return False
        return super(RegisterForm, self).validate()

    def to_dict(self):
        def is_field_and_user_attr(member):
            return isinstance(member, Field) and \
                hasattr(User, member.name)

        fields = inspect.getmembers(self, is_field_and_user_attr)
        return dict((key, value.data) for key, value in fields)


class LoginForm(Form):
    email_or_name = StringField('email_or_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=30)])
    captcha = CaptchaField()
    next = HiddenField()

    def validate_next(self, field):
        from flask_security.utils import validate_redirect_url
        if field.data and not validate_redirect_url(field.data):
            field.data = ''
            flash('INVALID_REDIRECT')
            raise ValidationError('INVALID_REDIRECT')

    def validate_email_or_name(self, field):
        from sqlalchemy import or_
        if not User.query.filter(or_(User.email==field.data, User.name==field.data)).first():
            raise ValidationError('email/name of password error')

    def validate(self):
        # always do captcha validate first
        captcha = self.captcha.data
        try:
            if not captcha:
                raise ValidationError('captcha is required')
            check_captcha(captcha)
        except ValidationError as e:
            self.captcha.errors += (str(e), )
            return False
        if not super(LoginForm, self).validate():
            return False
        from sqlalchemy import or_
        email_or_name = self.email_or_name.data
        password = self.password.data
        users = User.query.filter((User.email==email_or_name)|(User.name==email_or_name))
        user = users[0]
        from .utils import verify_and_update_password
        if not verify_and_update_password(password, user):
            self.email_or_name.errors.append('email/name or password error')
            self.password.errors.append('email/name or password error')
            #import ipdb; ipdb.set_trace()
            return False
        self.user = user
        return True
