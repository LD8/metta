from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    '''registering a new account'''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('forum:topics')

    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    '''render user's profile page'''
    posts = request.user.post_set.all()
    comments = request.user.comment_set.all()
    comments_on_posts_not_authored_by_me = []
    for comment in comments:
        if comment.post not in posts:
            comments_on_posts_not_authored_by_me.append(comment)
    return render(request, 'users/profile.html', {
        'posts': posts,
        'comments': comments,
        'other_comments': comments_on_posts_not_authored_by_me})
