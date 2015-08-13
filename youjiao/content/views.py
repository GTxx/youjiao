from flask import Blueprint, render_template

from .models import Activity

content_bp = Blueprint("activity_content", __name__)


@content_bp.route('/activity/<id>')
def activity_view(id):
    obj = Activity.query.get(id)
    return render_template('activity/activity.html', activity=obj)


@content_bp.route('/school/')
def school():
    return render_template('school/school.html')


@content_bp.route('/school/lectures/')
def school_sub():
    return render_template('school/home.html')

@content_bp.route('/category/<category>/')
def category(category):
    posts = Activity.query.filter_by(category=category).filter_by(status=2).all()
    return render_template('activity/home.html', activity_list=posts)
