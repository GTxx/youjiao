from youjiao.admin_utils import AuthEditorMixin
from flask_admin import AdminIndexView, expose


class YJHomeView(AuthEditorMixin, AdminIndexView):
    @expose()
    def index(self):
        from youjiao.user.models import User, Role
        from youjiao.content.models import Activity, Page
        from youjiao.teach_material.models import Courseware, Book
        from youjiao.onlinecourse.models import OnlineCourse
        from youjiao.yj_media.models import Video, Audio, Document
        from youjiao.photo.models import Photo, Album
        return self.render('yj_admin/dashboard.html', User=User, Role=Role, Activity=Activity,
                           Courseware=Courseware, Book=Book, Page=Page, OnlineCourse=OnlineCourse,
                           Video=Video, Audio=Audio, Document=Document, Photo=Photo, Album=Album)
