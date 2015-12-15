# -*- coding: utf-8 -*-

from __future__ import absolute_import
from flask import Blueprint, render_template, abort, request
from flask_login import current_user
from youjiao.user_util.models import Comment
from sqlalchemy import and_, or_
from youjiao.content.models import Slider
from .models import Book, Courseware
from .permissions import book_preview_permission, courseware_preview_permission

book_bp = Blueprint("book_view", __name__)


@book_bp.route('/book')
def book():
    teach_book_list = Book.query.filter(
        and_(Book.category == u'幼教教材', Book.publish == True)).limit(9)
    read_book_list = Book.query.filter_by(category=u'幼教读物').limit(9)
    # import ipdb; ipdb.set_trace()
    return render_template('book/home.html', teach_book_list=teach_book_list,
                           read_book_list=read_book_list, Book=Book,
                           slider=Slider.book_slider())


@book_bp.route('/book/list')
def book_list():
    level = request.args.get('level')
    book_list = Book.query.filter(Book.publish==True)
    if level:
        book_list = book_list.filter(Book.level==level)
    return render_template('book/list.html', book_list=book_list, level=level)


@book_bp.route('/book/<category>')
def book_category(category):
    if category == 'teach_book':
        level = request.args.get('level')
        book_list = Book.query.filter(Book.publish==True, Book.category==u'幼教教材')
        if level:
            book_list = book_list.filter(Book.level==level)
        book_list = book_list.limit(8)
        top10 = Book.top10()
        return render_template('book/sub_node.html', book_list=book_list, top10=top10,
                               level=level, slider=Slider.book_slider())

    elif category == 'read_book':
        book_list = Book.query.filter_by(category=u'幼教读物').limit(9)
        return render_template('book/sub_node.html', book_list=book_list)
    else:
        abort(404)


@book_bp.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    if not book.publish and not book_preview_permission.can():
        abort(404)

    if current_user.is_authenticated:
        book.add_user_visit_recent(current_user)

    page_comment = Comment.query.filter(
        and_(Comment.comment_obj_type == 'book',
             Comment.comment_obj_id == book.id)).paginate(1)
    return render_template('book/detail.html', book=book, obj=book,
                           page_comment=page_comment)


@book_bp.route('/book/associate/')
def book_associate():
    return render_template('book/associate.html')


@book_bp.route('/courseware/')
def courseware():
    courseware_list = Courseware.query.limit(12).all()
    return render_template('courseware/home.html', current_page='courseware',
                           courseware_list=courseware_list,
                           Courseware=Courseware, slider=Slider.courseware_slider())


@book_bp.route('/courseware/<int:courseware_id>/')
def courseware_detail(courseware_id):
    courseware = Courseware.query.get(courseware_id)
    if not courseware.publish and not courseware_preview_permission.can():
        abort(404)

    if current_user.is_authenticated:
        courseware.add_user_visit_recent(current_user)

    page_comment = Comment.query.filter(
        and_(Comment.comment_obj_type == 'courseware',
             Comment.comment_obj_id == courseware.id)).paginate(1)
    return render_template('courseware/detail.html', current_page='courseware',
                           courseware=courseware, page_comment=page_comment,
                           obj=courseware)


@book_bp.route('/courseware/list/')
def courseware_list():
    level = request.args.get('level')
    search = request.args.get('search')
    courseware_list = Courseware.query.outerjoin(Book).filter(Courseware.publish == True)
    if search:
        courseware_list = courseware_list.filter(
            or_(Courseware.name.like(u'{}%'.format(search)),
                Book.name.like(u'{}%'.format(search)),
                (Book.name + Courseware.name) == search)
        )
    if level:
        courseware_list = courseware_list.filter(Book.level == level)
    courseware_list = courseware_list.all()
    return render_template('courseware/list.html', current_page='courseware',
                           courseware_list=courseware_list, level=level)


@book_bp.route('/courseware/sub/')
def courseware_sub():
    top10 = Courseware.top10()
    level = request.args.get('level')
    if not level:
        courseware_list = Courseware.query.limit(10).all()
    elif level in [u'小班', u'中班', u'大班']:
        courseware_list = Courseware.query.join(Book).filter(Book.level == level).all()
    else:
        courseware_list = []
    return render_template('courseware/sub_node.html', current_page='courseware',
                           top10=top10, courseware_list=courseware_list,
                           slider=Slider.courseware_slider())


from youjiao.flask_qiniu import get_private_url


@book_bp.app_template_filter('qiniu_private_url')
def qiniu_private_url(key):
    return get_private_url(key)
