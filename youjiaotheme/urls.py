from django.conf.urls import url, patterns
from .views import youjiao

urlpatterns = patterns('',
                       (r'^youjiao/$', youjiao),
                       )
