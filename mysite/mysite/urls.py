from django.contrib import admin
from django.urls import path
from blog.views import post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/", post),
]