# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from .models import Activity

content_bp = Blueprint("activity_content", __name__)



@content_bp.route('/category/<category>/<page>/')
def category(category, page):
    try:
        page = int(page)
    except ValueError:
        page = 1

    pagination = Activity.query.filter_by(category=category).filter_by(status=True).paginate(page, per_page=20)
    category_dict = {
        'policy': u'幼教政策',
        'news': u'幼教新闻',
        'events': u'幼教事件',
        'research': u'理论研究',
        'activity': u'实践活动'
    }
    category_name = category_dict[category]
    return render_template('activity/home.html', activity_list=pagination, category_name=category_name,
                           category_url=category, current_page='activity')


@content_bp.route('/activity/<id>/')
def activity_view(id):
    obj = Activity.query.get(id)
    category_dict = {
        'policy': u'幼教政策',
        'news': u'幼教新闻',
        'events': u'幼教事件',
        'research': u'理论研究',
        'activity': u'实践活动'
    }
    category_name = category_dict[obj.category]
    return render_template('activity/activity.html', activity=obj, category_name=category_name,
                           current_page='activity')


@content_bp.route('/school/')
def school():
    return render_template('school/school.html', current_page='school')


@content_bp.route('/school/lectures/')
def school_sub():
    return render_template('school/home.html', current_page='school')


@content_bp.route('/school/teacher/')
def school_teacher():
    return render_template('school/teacher_training.html', current_page='school')


@content_bp.route('/school/product/')
def school_product():
    return render_template('school/product_training.html', current_page='school')


@content_bp.route('/school/product/detail/')
def school_teacher_detail():
    return render_template('school/t_t_detail.html', current_page='school')


@content_bp.route('/courseware/')
def courseware():
    return render_template('courseware/home.html', current_page='courseware')


@content_bp.route('/courseware/detail/')
def courseware_detail():
    return render_template('courseware/detail.html', current_page='courseware')


@content_bp.route('/courseware/list/')
def courseware_list():
    return render_template('courseware/list.html', current_page='courseware')


@content_bp.route('/courseware/sub/')
def courseware_sub():
    return render_template('courseware/sub_node.html', current_page='courseware')


@content_bp.route('/research/home/')
def research_home():
    research_events = Activity.query.filter_by(category='research').filter_by(status=2).limit(7).all()
    research_result = Activity.query.filter_by(category='researchresult').filter_by(status=2).limit(7).all()
    data = {
        'research_events': research_events,
        'research_result': research_result
    }
    return render_template('research/home.html', data=data, current_page='research')


@content_bp.route('/research/<category>/<page>/')
def research_activity(category, page):
    try:
        page = int(page)
    except ValueError:
        page = 1

    pagination = Activity.query.filter_by(category=category).filter_by(status=2).paginate(page, per_page=20)
    category_dict = {
        'researchevents': u'教研活动',
        'researchresult': u'教研成果'
    }
    category_name = category_dict[category]
    return render_template('research/research_activity.html', category_name=category_name, activity_list=pagination,
                           current_page='research')


@content_bp.route('/research/post/<id>')
def research_post(id):
    obj = Activity.query.get(id)
    category_dict = {
        'researchevents': u'教研活动',
        'researchresult': u'教研成果'
    }
    category_name = category_dict[obj.category]
    return render_template('research/research_activity_content.html', category_name=category_name, activity=obj,
                           current_page='research')


@content_bp.route('/research/teacher/')
def research_teacher():
    return render_template('research/teacher.html', current_page='research')


@content_bp.route('/page/about/')
def page_about():
    return render_template('pages/about.html')
