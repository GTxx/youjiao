# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, abort

from .permissions import content_preview_permission

from .models import Activity, OnlineCourse, Page

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


@content_bp.route('/school/')
def school():
    return render_template('school/home.html', current_page='school',
                           Video=OnlineCourse)


@content_bp.route('/video/<int:video_id>')
def video_detail(video_id):
    video = OnlineCourse.query.get_or_404(video_id)
    if not video.publish and not content_preview_permission.can():
        abort(404)
    return render_template('school/video_detail.html', video=video)


@content_bp.route('/school/<category>/')
def school_sub(category):
    if category == 'lecture':
        video_list = OnlineCourse.query.filter(OnlineCourse.category==u'优秀讲座').limit(9)
        return render_template('school/sub_node.html', current_page='school',
                               video_list=video_list)
    else:
        abort(404)


@content_bp.route('/school/teacher/')
def school_teacher():
    return render_template('school/teacher_training.html', current_page='school')


@content_bp.route('/school/product/')
def school_product():
    return render_template('school/product_training.html', current_page='school')


@content_bp.route('/school/product/detail/')
def school_teacher_detail():
    return render_template('school/video_detail.html', current_page='school')


@content_bp.route('/research/home/')
def research_home():
    research_events = Activity.query.filter_by(category='research').filter_by(publish=True).limit(7).all()
    research_result = Activity.query.filter_by(category='achievement').filter_by(publish=True).limit(7).all()
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

    pagination = Activity.query.filter_by(category=category).filter_by(publish=True).paginate(page, per_page=20)
    category_dict = {
        'event': u'教研活动',
        'achievement': u'教研成果'
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


@content_bp.route('/page/<page_title>/')
def pages(page_title):
    content = Page.query.filter_by(title=page_title).first()
    return render_template('pages/tpl.html', content=content, obj=content)
