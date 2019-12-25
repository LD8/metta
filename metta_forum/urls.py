from django.urls import path
from . import views

app_name = 'metta_forum'
urlpatterns = [
	path('', views.index, name='index'),
	path('boards/', views.boards, name='boards'),
	path('boards/<int:board_pk>', views.board, name='board'),
	path('boards/board/<int:topic_pk>', views.topic, name='topic'),
	path('boards/board/topic/<int:post_pk>', views.post, name='post'),
]