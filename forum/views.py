from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Post, Comment
from .forms import TopicForm, PostForm, CommentForm
# Q helps to search A or B at the same time
from django.db.models import Q


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
    topics = Topic.objects.order_by('-date_added')
    return render(request, 'forum/topic.html', {'topic': topic, 'topics': topics})


def post(request, topic_pk, post_pk, comment_pk=None):
    '''displaying one post under a topic and all the comments under this post'''
    # get existing topic and post
    topic = get_object_or_404(Topic, pk=topic_pk)
    try:
        post = topic.post_set.get(pk=post_pk)
    except:
        raise Http404

    # get all the comments under this post
    comments = post.comment_set.all()

    # deal with comment editing
    if comment_pk != None:
        comment_to_be_edited = get_object_or_404(Comment, pk=comment_pk)

        if 'delete' in request.POST:
            comment_to_be_edited.delete()
            return redirect('forum:post', topic_pk, post_pk)
        
        # get form with existing data ready to be rendered or edited/updated
        edit_comment_form = CommentForm(instance=comment_to_be_edited)

        if 'update' in request.POST:
            edit_comment_form = CommentForm(instance=comment_to_be_edited, data=request.POST)
            if edit_comment_form.is_valid():
                edit_comment_form.save()
                return redirect('forum:post', topic_pk, post_pk)

        # if not to delete or to update, simply render the existing form with comment data ready to be edited
        return render(request, 'forum/post.html', {
                'topic': topic,
                'post': post,
                'comments': comments,
                'comment_to_be_edited': comment_to_be_edited,
                'edit_comment_form': edit_comment_form})

    # if not posting a new comment, simply render the form
    if request.method != 'POST':
        form = CommentForm()
    else:
        # deal with posting a new comment
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('forum:post', topic_pk, post_pk)

    # render the post and all the comments and the empty/error form
    return render(request, 'forum/post.html', {
        'topic': topic,
        'post': post,
        'comments': comments,
        'form': form})


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


def search(request, query=None, topic_pk=None):
    # if no-input submission --> redirect to topics for users to browse
    if request.GET.get('query') == '':
        return redirect('forum:topics')

    # if user searching from nav bar, get the request query value stored properly
    if query == None:
        query = request.GET.get('query')

    # search through all Post objects, in titles and contents
    search_result_posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(date_added__icontains=query))

    # because there are only a few topics,
    # use filtered posts to determine topics for displaying in the sidebar
    search_result_topics = []
    for post in search_result_posts:
        if post.topic not in search_result_topics:
            search_result_topics.append(post.topic)

    # passing an empty topic if topic_pk=None
    search_result_topic = {}

    # if to check results in a specific topic
    if topic_pk != None:
        # make sure this topic exists and override the default value
        search_result_topic = get_object_or_404(Topic, pk=topic_pk)
        # search through all the posts in this topic, and override previous search_results_posts
        search_result_posts = search_result_topic.post_set.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query))

    return render(request, 'forum/search.html', {
        'search_result_posts': search_result_posts,
        'search_result_topics': search_result_topics,
        'search_result_topic': search_result_topic,
        'query': query})
