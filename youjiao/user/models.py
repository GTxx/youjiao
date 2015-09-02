# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import RoleMixin, UserMixin, SQLAlchemyUserDatastore
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
from captcha.image import ImageCaptcha
import os
import time
from .utils import generate_random_number_4, encrypt_password, \
    verify_password, get_hmac, password_context


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    phone_number = db.Column(db.String(16), unique=True)
    active = db.Column(db.Boolean, default=True)
    # is_admin = db.Column(db.Boolean, default=False)
    # TODO: use a base model to add create_time and update_time
    create_time = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime, onupdate=datetime.now)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    profile = db.relationship('UserProfile', backref='user', uselist=False)

    def __repr(self):
        return '<User {}>'.format(self.name)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def create_user(cls, name, email, password):
        from .utils import encrypt_password
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


class UserProfile(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    # TODO: one to one relation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # TODO: add column describe/description
    work_place_name = db.Column(db.String(255))
    avatar = db.Column(db.String(200), default='default.png')


class Role(db.Model, RoleMixin, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Captcha(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True)
    content = db.Column(db.String(4), default=generate_random_number_4)
    img_name = db.Column(db.String(128))

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