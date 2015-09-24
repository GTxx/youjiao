# -*- coding: utf-8 -*-

from __future__ import absolute_import
from flask import Blueprint, render_template, abort
from youjiao.user_util.models import Comment
from sqlalchemy import and_
from .models import Book

book_bp = Blueprint("book_view", __name__)


@book_bp.route('/book')
def book():
    teach_book_list = Book.query.filter_by(category=u'幼教教材').limit(9)
    read_book_list = Book.query.filter_by(category=u'幼教读物').limit(9)
    # import ipdb; ipdb.set_trace()
    return render_template('book/home.html', teach_book_list=teach_book_list,
                           read_book_list=read_book_list, Book=Book)


@book_bp.route('/book/upload')
def book_upload():
    return render_template('book/upload.html')


@book_bp.route('/book/<category>')
def book_category(category):
    if category == 'teach_book':
        book_list = Book.query.filter_by(category=u'幼教教材').limit(9)
        top10 = Book.top10()
        return render_template('book/sub_node.html', book_list=book_list, top10=top10)

    elif category == 'read_book':
        book_list = Book.query.filter_by(category=u'幼教读物').limit(9)
        return render_template('book/sub_node.html', book_list=book_list)
    else:
        abort(404)


@book_bp.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    page_comment = Comment.query.filter(
        and_(Comment.comment_obj_type == 'book',
             Comment.comment_obj_id == book.id)).paginate(1)
    return render_template('book/detail.html', book=book,
                           page_comment=page_comment)
