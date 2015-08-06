from django.conf.urls import url, patterns
from .views.views import *
from .views.account_view import *

urlpatterns = patterns('',
                       (r'^activities/(\D+)/(\d+)$', activities),
                       (r'^activities/(\d+)$', blog_detail),
                       (r'^products/(\D+)$', products),
                       (r'^products/textbook/1', text_book_detail),
                       (r'^account/login/$', LoginView.as_view()),
                       (r'^account/register/', RegisterView.as_view()),
                       )
