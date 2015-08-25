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


@content_bp.route('/product/')
def product():
    return render_template('product/home.html')


@content_bp.route('/product/detail/')
def product_detail():
    return render_template('product/detail.html')


@content_bp.route('/product/sub/')
def product_sub():
    return render_template('product/sub_node.html')


@content_bp.route('/courseware/')
def courseware():
    return render_template('courseware/home.html')


@content_bp.route('/courseware/detail/')
def courseware_detail():
    return render_template('courseware/detail.html')


@content_bp.route('/courseware/list/')
def courseware_list():
    return render_template('courseware/list.html')


@content_bp.route('/courseware/sub/')
def courseware_sub():
    return render_template('courseware/sub_node.html')


@content_bp.route('/courseware/teacher/')
def courseware_teacher():
    return render_template('courseware/teacher_training.html')


@content_bp.route('/courseware/product/')
def courseware_product():
    return render_template('courseware/product_training.html')


@content_bp.route('/courseware/teacher/detail/')
def courseware_teacher_detail():
    return render_template('courseware/t_t_detail.html')


@content_bp.route('/research/teacher/')
def research_teacher():
    return render_template('research/teacher.html')


@content_bp.route('/page/about/')
def page_about():
    return render_template('pages/about.html')
