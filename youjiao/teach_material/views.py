# -*- coding: utf-8 -*-

from __future__ import absolute_import
from flask import Blueprint, render_template, abort, request
from flask_login import current_user
from youjiao.user_util.models import Comment
from sqlalchemy import and_, or_
from youjiao.content.models import Slider
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs
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


book_args = {
    'level': fields.Str(missing='', validate=validate.OneOf(Book.level_list+[''])),
    'search': fields.Str(missing='')
}

@book_bp.route('/book/list')
@use_kwargs(book_args)
def book_list(level, search):
    # level = request.args.get('level')
    query = Book.query.filter(Book.publish==True)
    if level:
        query = query.filter(Book.level==level)
    if search:
        query = query.filter(Book.name.like(u'%{}%'.format(search)))
    return render_template('book/list.html', book_list=query, level=level,
                           search=search)


@book_bp.route('/book/<category>')
@use_kwargs({'level': fields.Str(validate=lambda level: level in Book.level_list)})
def book_category(category, level):
    # level = request.args.get('level')
    if category == 'teach_book':
        book_list = Book.query.filter(Book.publish==True, Book.category==u'幼教教材')
        if level:
            book_list = book_list.filter(Book.level==level)
        book_list = book_list.limit(8)
        top10 = Book.top10()
        return render_template('book/sub_node.html', book_list=book_list, top10=top10,
                               level=level, slider=Slider.book_slider(), category=category)

    elif category == 'read_book':
        book_list = Book.query.filter(Book.publish==True, Book.category==u'幼教读物')
        if level:
            book_list = book_list.filter(Book.level==level)
        book_list = book_list.limit(8)
        return render_template('book/sub_node.html', book_list=book_list, level=level,
                               slider=Slider.book_slider(), category=category)
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


courseware_args = {
    'level': fields.Str(missing='', validate=validate.OneOf(Courseware.level_list+[''])),
    'search': fields.Str(missing='')
}


@book_bp.route('/courseware/list/')
@use_kwargs(courseware_args)
def courseware_list(level, search):
    # import ipdb; ipdb.set_trace()
    courseware_list = Courseware.query.outerjoin(Book).filter(Courseware.publish==True)
    if search:
        courseware_list = courseware_list.filter(
            or_(Courseware.name.like(u'{}%'.format(search)),
                Book.name.like(u'{}%'.format(search)),
                (Book.name + Courseware.name) == search)
        )
    if level:
        courseware_list = courseware_list.filter(Courseware.level==level)
    courseware_list = courseware_list.all()
    return render_template('courseware/list.html', current_page='courseware',
                           courseware_list=courseware_list, level=level,
                           search=search)


@book_bp.route('/courseware/sub/')
@use_args(courseware_args)
def courseware_sub(args):
    top10 = Courseware.top10()
    level = args.get('level')
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
