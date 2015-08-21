# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import RoleMixin, UserMixin, SQLAlchemyUserDatastore
from flask_security import Security
from youjiao.extensions import db
from youjiao.utils.database import CRUDMixin
from captcha.image import ImageCaptcha
import os


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
    is_admin = db.Column(db.Boolean, default=False)
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


class UserProfile(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # TODO: add column describe/description
    work_place_name = db.Column(db.String(255))
    avatar = db.Column(db.String(200), default='default.png')


class Role(db.Model, RoleMixin, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)


from .utils import generate_random_number_4, generate_random_string_64
class Captcha(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(64), default=generate_random_string_64)
    content = db.Column(db.String(4), default=generate_random_number_4)

    @classmethod
    def generate(cls):
        captcha = cls()
        captcha.save()
        image = ImageCaptcha()
        # TODO: use file path config
        current_path = os.getcwd()
        image.write(captcha.content, os.path.join(current_path, 'youjiao/static/captcha', captcha.key+'.png'))
        return captcha

    @property
    def img_url(self):
        # TODO: use file path config
        return os.path.join('/static/captcha', self.key+'.png')

    def delete(self):
        file_name = os.path.join(os.getcwd(), 'youjiao/static/captcha', self.key+'.png')
        super(Captcha, self).delete()
        os.remove(file_name)

