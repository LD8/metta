from django.shortcuts import render, get_object_or_404
from .models import Board, Topic, Post

# Create your views here.
def index(request):
    '''
    Landing page:
    1. view without signing in
    2. sign in for old users
    3. sign up for new users
    '''
    return render(request, 'metta_forum/index.html')

def boards(request):
    '''
    Forum first page:
    show all boards as cards for users to choose
    '''
    boards = Board.objects.all()
    return render(request, 'metta_forum/boards.html', {'boards': boards})

def board(request, board_pk):
    '''
    A single board page:
    contains many topics displaying for users to click
    '''
    board = get_object_or_404(Board, pk=board_pk)
    topics = board.topic_set.all()
    return render(request, 'metta_forum/board.html', {'topics':topics, 'board': board})

def topic(request, topic_pk):
    '''
    A single topic page:
    contains many topics related to the subject/board
    '''
    topic = get_object_or_404(Topic, pk=topic_pk)
    posts = topic.post_set.all()
    return render(request, 'metta_forum/topic.html', {'topic':topic, 'posts':posts})

def post(request, post_pk):
    '''
    A single post page:
    to display the post only
    '''
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'metta_forum/post.html', {'post':post})