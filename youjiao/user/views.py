from flask import Blueprint, render_template


user_bp = Blueprint("user_view", __name__)


@user_bp.route('/account/login/')
def login():
    return render_template('account/login.html')


@user_bp.route('/account/register/')
def register():
    return render_template('account/register.html')

