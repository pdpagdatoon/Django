from django import forms
from .models import Comment
from .models import Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']