from django.conf.urls import url, include
from course_management_system.courses import views


urlpatterns = [
    url(r'$^', views.course_index),
    url(r'new/', views.create_course),
    url(r'edit/(?P<course_name>[A-Za-z0-9]+)/$', views.edit_course),
    url(r'(?P<course_name>[A-Za-z0-9]+)/$', views.course_info)
]
