"""DJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from bird import views
urlpatterns = [
    url(r'^$','bird.views.index',name='index'),
    url(r'reg/$','bird.views.register',name='register'),
    url(r'login/$','bird.views.login',name='login'),
    url(r'upload/$','bird.views.upload',name='upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^img/(?P<user>\w+)/', 'bird.views.user_img'),
    url(r'add_update$','bird.views.new_update',name='new_update'),
    url(r'follow_user$', 'bird.views.follow_user', name='follow_user'),
    url(r'search_user$', 'bird.views.search_users', name='search_user'),
    url(r'like_update$', 'bird.views.like_update', name='like_update'),
