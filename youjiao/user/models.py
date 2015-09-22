# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from flask_security import RoleMixin
from flask_login import UserMixin
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
from captcha.image import ImageCaptcha
import sqlalchemy as sqla
import os
import time
from .utils import generate_random_number_4, encrypt_password, \
    verify_password, get_hmac, password_context


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', sqla.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', sqla.Integer(), db.ForeignKey('role.id')),
    sqla.UniqueConstraint('user_id', 'role_id')
)

class User(db.Model, UserMixin, CRUDMixin):
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(50), unique=True)
    email = db.Column(sqla.String(50), unique=True)
    password = db.Column(sqla.String(200))

    phone_number = db.Column(sqla.String(16), unique=True)
    active = db.Column(sqla.Boolean, default=True)
    # is_admin = db.Column(db.Boolean, default=False)
    # TODO: use a base model to add create_time and update_time
    create_time = db.Column(sqla.DateTime, default=datetime.utcnow)
    last_login = db.Column(sqla.DateTime)

    # TODO: add login log field, and add field update in login view
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    profile = db.relationship('UserProfile', backref='user', uselist=False)
    from youjiao.user_util.models import Comment, Favor
    comments = db.relationship('Comment', backref='user')
    favors = db.relationship('Favor', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.name)

    @classmethod
    def create_user(cls, name, email, password):
        password = encrypt_password(password)
        user = User()
        user.name = name
        user.email = email
        user.password = password
        user.save()
        return user

    def set_password(self, new_password):
        self.password = encrypt_password(new_password)
        self.save()

    def verify_password(self, password):
        return verify_password(password, self.password)

    def verify_and_update_password(self, password):
        """used in login user"""
        signed = get_hmac(password).decode('ascii')
        verified, new_password = password_context.verify_and_update(signed, self.password)
        if verified and new_password:
            self.password = new_password
            self.save()
        return verified

    @property
    def roles_name(self):
        return [role.name for role in self.roles]

    def favor(self, obj_type):
        from youjiao.user_util.models import Favor
        pass


class UserProfile(db.Model, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    user_id = db.Column(sqla.Integer, db.ForeignKey('user.id'))
    # TODO: add column describe/description
    nickname = db.Column(sqla.String(16), unique=True)
    work_place_name = db.Column(sqla.String(255))
    avatar_qiniu_key = db.Column(sqla.String(200), default='default_avatar.png')
    birthday = db.Column(sqla.Date)
    gender = db.Column(sqla.Enum('male', 'female', name='gender'))
    career = db.Column(sqla.String(16))
    province = db.Column(sqla.String(16))
    city = db.Column(sqla.String(16))
    district = db.Column(sqla.String(16))
    street = db.Column(sqla.String(16))

    @property
    def location(self):
        return '{} {} {} {}'.format(self.province, self.city, self.district, self.street)


class Role(db.Model, RoleMixin, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    name = db.Column(sqla.String(80), unique=True)
    description = db.Column(sqla.String(255))

    def __repr__(self):
        return '<Role {}>'.format(self.name)


# TODO: use redis expire
class Captcha(db.Model, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    key = db.Column(sqla.String(64), unique=True)
    content = db.Column(sqla.String(4), default=generate_random_number_4)
    img_name = db.Column(sqla.String(128))

    @classmethod
    def generate(cls, key):
        captcha = cls.query.filter_by(key=key).first()
        if not captcha:
            captcha = cls()
        captcha.key = key
        captcha.content = generate_random_number_4()
        captcha.save()
        image = ImageCaptcha(width=160, height=80)
        img_buffer = image.generate(captcha.content)
        captcha.img_string = img_buffer.read()
        return captcha

    @classmethod
    def get_b64_img(cls, img_string):
        # NOTE: ie8 not support image > 32k
        import base64
        b64_string = base64.b64encode(img_string)
        return "data:image/png;base64,{}".format(b64_string)
