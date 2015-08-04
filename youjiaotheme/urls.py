from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
                       (r'^activities/(\D+)/(\d+)$', activities),
                       (r'^activities/(\d+)$', blog_detail)
                       )
