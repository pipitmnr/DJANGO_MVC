from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('tambah-blog/', views.addBlog, name='add-blog'),
    path('post-blog/', views.postBlog, name='post-blog'),
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor, name='mentor'),
    path('author/', views.author, name='author'),
]