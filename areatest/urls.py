# -*- coding: UTF-8 -*-
from django.conf.urls import url
from areatest import views


urlpatterns =[
    url(r'^area/$', views.area),
    url(r'^pro/$', views.pro),
    url(r'^city/(\d+)/$', views.city),
    url(r'^dis/(\d+)/$', views.dis),
    url(r'^editor/$', views.editor),
    url(r'^editorhandle/$', views.editorhandle),

    url(r'^cacheview/$', views.cacheview),

    url(r'^mysearch/$', views.mysearch)
]
