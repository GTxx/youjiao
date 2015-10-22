from youjiao.admin_utils import AuthEditorMixin
from flask_admin import AdminIndexView, expose


class YJHomeView(AuthEditorMixin, AdminIndexView):

    @expose()
    def index(self):
        from youjiao.user.models import User
        from youjiao.content.models import Activity
        from youjiao.teach_material.models import Courseware, Book
        return self.render('yj_admin/dashboard.html', User=User,
                           Activity=Activity, Courseware=Courseware, Book=Book)
