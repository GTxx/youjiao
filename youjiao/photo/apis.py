from flask import views, jsonify, Blueprint, request
from flask_login import login_required
from webargs import fields, validate
from webargs.flaskparser import use_args
from .models import Photo, Album
from .schemas import PhotoSchema, AlbumSchema, PaginatePhotoSchema


photo_api_bp = Blueprint("photo_api", __name__)


class PhotoListView(views.MethodView):
    methods = ['GET', 'POST']
    decorators = [login_required, ]
    photolist_schema = PhotoSchema(many=True)
    paginatephotolist_schema = PaginatePhotoSchema()
    photo_args = {
        'search': fields.Str(),
        'page': fields.Int(missing=1),
        'page_size': fields.Int(missing=10)
    }

    @use_args(photo_args)
    def get(self, args):
        # get query
        # TODO: get query based on user type
        # import ipdb; ipdb.set_trace()
        query = Photo.query
        # filter
        # search
        search_keyword = request.args.get('search')
        if search_keyword:
            query = query.filter(Photo.name.like(u'%{}%'.format(search_keyword)))
        # paginate
        page = args['page']
        page_size = args['page_size']
        paginate = query.paginate(page=page, per_page=page_size )
        content = {
            'results': paginate.items,
            'count': paginate.total,
            'next': paginate.next_num if paginate.has_next else None,
            'prev': paginate.prev_num if paginate.has_prev else None,
        }
        # filter
        # search
        # serializer
        results = self.paginatephotolist_schema.dump(content)
        return jsonify(results.data)

    def post(self):
        pass


class PhotoView(views.MethodView):
    methods = ['GET', 'PUT', 'DELETE']
    # TODO: add permissions
    decorators = [login_required, ]
    photo_schema = PhotoSchema()

    def get(self, pk=None):
        photo = Photo.query.get_or_404(pk)
        results = self.photo_schema.dump(photo)
        return jsonify(results.data)

    def put(self):
        pass

    def delete(self, pk=None):
        pass


photo_api_bp.add_url_rule('/api/photo/', view_func=PhotoListView.as_view('photo_api'), endpoint='photo_api')
photo_api_bp.add_url_rule('/api/photo/<int:pk>', view_func=PhotoView.as_view('photo_detail_api'), endpoint='photo_detail_api')
