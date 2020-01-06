from django import forms
from .models import Topic, Post, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        labels = {'name': 'Topic', 'description': "What's this topic about?"}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Title', 'content': 'Text' }
        widgets = {'content': forms.Textarea(attrs={'col': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3})}