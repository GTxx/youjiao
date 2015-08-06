from django.conf.urls import url, patterns
from .views import *
from .account_view import *

urlpatterns = patterns('',
                       (r'^activities/(\D+)/(\d+)$', activities),
                       (r'^activities/(\d+)$', blog_detail),
                       (r'^products/(\D+)$', products),
                       (r'^products/textbook/1', text_book_detail),
                       (r'^account/login/$', LoginView.as_view()),
                       )
