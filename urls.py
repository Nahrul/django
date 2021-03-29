from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', include('about.urls')),
    path('blog', include('blog.urls')),
    path('', views.index),

]
