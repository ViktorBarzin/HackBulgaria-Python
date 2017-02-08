from django.conf.urls import url, include
from django.contrib import admin
from course_management_system.lectures import views

urlpatterns = [
    url(r'new/$', views.create_lecture),
    url(r'edit/(?P<lecture_id>[0-9]+)', views.edit_lecture),
    url(r'(?P<lecture_id>[0-9]+)', views.show_lecture)
]
