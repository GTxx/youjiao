# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, abort
from .models import Activity, Page
from sqlalchemy import or_, and_


content_bp = Blueprint("activity_content", __name__)


@content_bp.route('/activity')
def activity():
    try:
        page = int(request.args.get('page'))
    except Exception as e:
        page = 1
    pagination = Activity.query.filter_by(publish=True).paginate(page, per_page=20)
    weekly_popular_top10 = Activity.weekly_popular_top10()
    return render_template('activity/home.html', activity_list=pagination,
                           category_url=category, current_page='activity', weekly_popular_top10=weekly_popular_top10)


@content_bp.route('/activity/<category>')
def category(category):
    try:
        page = int(request.args.get('page'))
    except Exception as e:
        page = 1

    pagination = Activity.query.filter_by(category=category).filter_by(publish=True).paginate(page, per_page=20)
    category_dict = {
        'policy': u'幼教政策',
        'news': u'幼教新闻',
        'events': u'幼教事件',
        'research': u'理论研究',
        'activity': u'实践活动'
    }
    category_name = category_dict[category]
    weekly_popular_top10 = Activity.weekly_popular_top10()
    return render_template('activity/home.html', activity_list=pagination, category_name=category_name,
                           category_url=category, current_page='activity', sub_page=category, weekly_popular_top10=weekly_popular_top10)


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
                           current_page='activity', obj=obj)

# 教学教研总页
@content_bp.route('/page/home/')
def page_home():
    teacher_kindergarten = Page.query.filter(or_(Page.status=='0', Page.status=='1')).filter(Page.publish==True).order_by('-id').limit(3)
    achievement = Page.query.filter_by(status='2').filter(Page.publish==True).limit(10).all()
    data = {
        'teacher_kindergarten': teacher_kindergarten,
        'achievement': achievement
    }
    return render_template('pages/home.html', data=data, current_page='research')


# 教研成果总页
@content_bp.route('/page/achievement/')
def page_activity():
    try:
        page = int(request.args.get('page'))
    except ValueError:
        page = 1

    pagination = Page.query.filter(Page.status=='2').filter(Page.publish==True).paginate(page, per_page=18)
    category_name = u'教研成果'
    return render_template('pages/research_activity.html', category_name=category_name, activity_list=pagination,
                           current_page='research')

# 教研成果单页
@content_bp.route('/page/achievement/<id>')
def page_post(id):
    obj = Page.query.get(id).filter(Page.publish==True)
    status_name = {
        # 'researchevents': u'教研活动',
        '2': u'教研成果'
    }
    # status_url = {
    #     '2': 'achievement'
    # }

    category_name = status_name[obj.status]
    return render_template('pages/research_activity_content.html', category_name=category_name, activity=obj,
                           current_page='research')

# 名师名园总页--名师
@content_bp.route('/page/teacher&kindergarten/teacher/')
def page_teacher():
    try:
        page = int(request.args.get('page'))
    except ValueError:
        page = 1
    teacher_pagination = Page.query.filter(Page.status=='0').filter(Page.publish==True).paginate(page, per_page=5)
    return render_template('pages/teacher.html', current_page='research', teacher_list=teacher_pagination)

# 名园
@content_bp.route('/page/teacher&kindergarten/kindergarten/')
def page_kindergarten():
    try:
        page = int(request.args.get('page'))
    except ValueError:
        page = 1
    kindergarten_pagination = Page.query.filter(Page.status=='1').filter(Page.publish==True).paginate(page, per_page=5)
    return render_template('pages/kindergarten.html', current_page='research',
                           kindergarten_list=kindergarten_pagination)

# 名师名园单页
@content_bp.route('/page/teacher&kindergarten/<page_id>/')
def pages(page_id):
    content = Page.query.filter_by(id=page_id).filter(Page.publish==True).first()
    return render_template('pages/tpl.html', content=content)


@content_bp.route('/page/about/')
def page_about():
    return render_template('pages/about.html')

