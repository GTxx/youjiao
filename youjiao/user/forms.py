# -*- coding: utf-8 -*-
from flask_login import current_user
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
from .models import User, UserProfile, RedisCaptcha
from .utils import verify_password


def unique_user_name(form, field):
    if User.query.filter_by(name=field.data).first() is not None:
        raise ValidationError(u'用户名已经存在')


def unique_email(form, field):
    if User.query.filter_by(email=field.data).first() is not None:
        raise ValidationError(u'email已经存在')


def check_captcha(captcha_content):
    captcha_key = session.get('captcha_key')
    if not RedisCaptcha.check(captcha_key, captcha_content):
        raise ValidationError(u'验证码错误')


def captcha_validator(form, field):
    return check_captcha(field.data)


class CaptcharWidget(object):
    def __call__(self, field, **kwargs):
        if 'captcha_key' not in session:
            session['captcha_key'] = hashlib.sha1(os.urandom(64)).hexdigest()
        captcha = RedisCaptcha(str(session['captcha_key']))
        return HTMLString('<img src="{}">'.format(captcha.b64_img))


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

    def validate(self):
        # always do captcha validate first
        captcha = self.captcha.data
        try:
            if not captcha:
                raise ValidationError(u'需要填写验证码')
            check_captcha(captcha)
        except ValidationError as e:
            self.captcha.errors += (unicode(e), )
            return False
        if not super(LoginForm, self).validate():
            return False
        email_or_name = self.email_or_name.data
        password = self.password.data
        user = User.verify(email_or_name, password)
        if not user:
            self.email_or_name.errors.append(u'用户名/邮箱 密码错误')
            self.password.errors.append(u'用户名/邮箱 密码错误')
            return False
        self.user = user
        return True


from wtforms_alchemy import ModelForm
from flask_wtf import Form as csrf_form
class UserProfileForm(csrf_form, ModelForm):
    nickname_validators = [DataRequired(), Length(min=4, max=15)]
    nickname = StringField(u'nickname', validators=nickname_validators)

    def validate_nickname(self, field):
        if not field.data == current_user.profile.nickname:
            if UserProfile.query.filter_by(nickname=field.data).first() is not None:
                raise ValidationError('nickname already exists')

    class Meta:
        model = UserProfile
        exclude = ['avatar_qiniu_key']


from wtforms.fields import FileField
class UserAvatarForm(csrf_form):
    avatar = FileField()


class ModifyPasswordForm(Form):
    old_password_validators = [DataRequired(), Length(min=6, max=15)]
    password_validators = [DataRequired(), Length(min=6, max=15)]
    password_confirm_validators = password_validators + [EqualTo('password', 'retry password mismatch')]

    old_password = StringField(u'old_password', validators=old_password_validators)
    password = StringField(u'password', validators=password_validators)
    password_confirm = StringField(u'password_confirm', validators=password_confirm_validators)

    def validate(self):
        if not super(ModifyPasswordForm, self).validate():
            return False
        # validate old password
        if not verify_password(self.old_password.data, current_user.password):
            self.old_password.errors.append(u'密码错误')
            return False
        return True

