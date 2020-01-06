from django.urls import path, include
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),

    # topic section
    path('topics/', views.topics, name='topics'),
    path('topic_<int:topic_pk>/', views.topic, name='topic'),

    # post section
    path('topic_<int:topic_pk>/new_post/', views.new_post, name='new_post'),
    path('topic_<int:topic_pk>/<int:post_pk>/', views.post, name='post'),
    path('topic_<int:topic_pk>/edit_<int:post_pk>/', views.edit_post, name='edit_post'),
    path('topic_<int:topic_pk>/<int:post_pk>/edit_<int:comment_pk>/', views.post, name='edit_comment'),

    # search section
    path('search/', views.search, name='search'),
    path('search/<query>/topic_<int:topic_pk>/', views.search, name='search_topic'),
]