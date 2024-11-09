# from django.conf.urls import url
# from . import views
# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
# ]

from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_home, name='blog_home'),
]
