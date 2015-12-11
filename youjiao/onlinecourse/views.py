# -*- coding: utf-8 -*-

from flask import Blueprint, abort, render_template
from youjiao.content.models import Slider
from .models import OnlineCourse
from .permissions import onlinecourse_preview_permission


online_course_bp = Blueprint("online_course", __name__)


@online_course_bp.route('/school/')
def school():
    slider = Slider.onlinecourse_slider()
    return render_template('onlinecourse/home.html', current_page='school',
                           Video=OnlineCourse, slider=slider)


@online_course_bp.route('/video/<int:video_id>')
def video_detail(video_id):
    video = OnlineCourse.query.get_or_404(video_id)
    if not video.publish and not onlinecourse_preview_permission.can():
        abort(404)
    return render_template('onlinecourse/video_detail.html', video=video)


@online_course_bp.route('/school/<category>/')
def school_sub(category):
    video_list = OnlineCourse.query.filter(OnlineCourse.publish==True)
    if category == 'lecture':
        video_list = video_list.filter(OnlineCourse.category==u'优秀讲座')
        slider = Slider.onlinecourse_slider()
        return render_template('onlinecourse/sub_node.html', current_page='school',
                               video_list=video_list, slider=slider)
    else:
        abort(404)


@online_course_bp.route('/school/teacher/')
def school_teacher():
    return render_template('onlinecourse/teacher_training.html', current_page='school')


@online_course_bp.route('/school/product/')
def school_product():
    return render_template('onlinecourse/product_training.html', current_page='school')


@online_course_bp.route('/school/product/detail/')
def school_teacher_detail():
    return render_template('onlinecourse/video_detail.html', current_page='school')

