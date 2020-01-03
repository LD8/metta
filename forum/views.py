from django.shortcuts import render, Http404,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Post
from .forms import TopicForm, PostForm


def index(request):
    '''landing page'''
    return render(request, 'forum/index.html')


def topics(request):
    '''displaying all the topics in sections with first 4 posts'''
    topics = Topic.objects.order_by('-date_added')
    return render(request, 'forum/topics.html', {'topics': topics})


def topic(request, topic_pk):
    '''displaying all the posts under one topic'''
    topic = get_object_or_404(Topic, pk=topic_pk)
    return render(request, 'forum/topic.html', {'topic': topic})


def post(request, topic_pk, post_pk):
    '''displaying one post under a topic'''
    topic = get_object_or_404(Topic, pk=topic_pk)
    try:
        post = topic.post_set.get(pk=post_pk)
    except:
        raise Http404
    return render(request, 'forum/post.html', {'topic': topic, 'post': post})


@login_required
def new_post(request, topic_pk):
    '''creating a new post'''
    topic = get_object_or_404(Topic, pk=topic_pk)
    if request.method != 'POST':
        form = PostForm()
    else:
        if 'save' in request.POST:
            form = PostForm(data=request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.topic = topic
                new_post.author = request.user
                new_post.save()
                return redirect('forum:topic', topic_pk=topic_pk)

    return render(request, 'forum/new_post.html', {'form': form, 'topic': topic})


@login_required
def edit_post(request, topic_pk, post_pk):
    '''editing/saving/deleting an existing post'''
    topic = get_object_or_404(Topic, pk=topic_pk)
    post = get_object_or_404(Post, pk=post_pk)
    if request.user != post.author:
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        if 'save' in request.POST:
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
        if 'delete' in request.POST:
            post.delete()
            return redirect('forum:topic', topic_pk=topic_pk)
        return redirect('forum:post', topic_pk=topic_pk, post_pk=post_pk)

    return render(request, 'forum/edit_post.html', {'form': form, 'topic': topic, 'post': post})
