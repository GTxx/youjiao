# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
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

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def check_password(self, password):
        return check_password_hash(self.password, password)

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


class UserProfile(db.Model, CRUDMixin):
    id = db.Column(sqla.Integer, primary_key=True)
    user_id = db.Column(sqla.Integer, db.ForeignKey('user.id'))
    # TODO: add column describe/description
    nickname = db.Column(sqla.String(16), unique=True)
    work_place_name = db.Column(sqla.String(255))
    avatar_qiniu_key = db.Column(sqla.String(200), default='default_avatar.png')
    birthday = db.Column(sqla.Date)
    gender = db.Column(sqla.Enum('male', 'female'))
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

    @property
    def img_path(self):
        return os.path.join(os.getcwd(), 'youjiao/static/captcha', self.img_name)

    @classmethod
    def generate(cls, key):
        captcha = cls.query.filter_by(key=key).first()
        if captcha:
            captcha.delete_img()
        else:
            captcha = cls()
        captcha.key = key
        captcha.content = generate_random_number_4()
        captcha.img_name = '.'.join([key, str(int(time.time())), 'png'])
        captcha.save()
        image = ImageCaptcha(width=160, height=80)
        # TODO: use file path config
        image.write(captcha.content, captcha.img_path)
        return captcha

    @property
    def img_url(self):
        # TODO: use file path config
        return os.path.join('/static/captcha', self.img_name)

    def delete(self):
        self.delete_img()
        super(Captcha, self).delete()

    def delete_img(self):
        try:
            os.remove(self.img_path)
        except Exception as e:
            print(e)