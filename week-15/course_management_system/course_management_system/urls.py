"""course_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from course_management_system.logged_in import views as logged_in_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', include('course_management_system.courses.urls')),
    url(r'^$', logged_in_views.login),
    url(r'^course/', include('course_management_system.courses.urls')),
    url(r'^lecture/', include('course_management_system.lectures.urls')),
    url(r'^register/$', logged_in_views.register),
    url(r'^login/$', logged_in_views.login),
    url(r'^profile$', logged_in_views.profile, name='profile'),
    url(r'^logout$', logged_in_views.logout)
]