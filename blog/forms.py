from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "image",
        ]

        widgets = {
            'content': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(BlogForm, self).__init__(*args, **kwargs)
