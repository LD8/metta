from django.urls import path, include
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic_<int:topic_pk>/', views.topic, name='topic'),
    path('topic_<int:topic_pk>/new_post/', views.new_post, name='new_post'),
    path('topic_<int:topic_pk>/<int:post_pk>/', views.post, name='post'),
    path('topic_<int:topic_pk>/<int:post_pk>/edit', views.edit_post, name='edit_post'),
]