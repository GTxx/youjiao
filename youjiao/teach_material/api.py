from flask import Blueprint, views, request, jsonify
from flask_login import login_required, current_user
from .models import Book
from youjiao.user_util.schemas import CommentSchema
from youjiao.user_util.models import Comment

book_api_bp = Blueprint('book_api_bp', __name__)


class BookCommentView(views.MethodView):
    methods = ['GET', 'POST']
    decorators = [login_required, ]

    def get(self, id):
        return 'book comment'

    def post(self, id):
        book = Book.query.get_or_404(id)
        data = request.get_json()
        content = data.get('content')
        if not content:
            return jsonify({'error': 'content empty'}), 400
        if len(content) > 140:
            return jsonify({'error': 'content too long'}), 400

        comment = Comment(user_id=current_user.id, comment_obj_id=book.id,
                comment_obj_type='book', content=content)
        comment.save()
        res = CommentSchema().dump(comment)
        return jsonify(res.data), 201


book_api_bp.add_url_rule('/api/book/<int:id>/comment', view_func=BookCommentView.as_view('book_comment'), endpoint='book_comment')
