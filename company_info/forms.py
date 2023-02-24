from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ContactUs, Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]

        widgets = {
            'content': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(BlogForm, self).__init__(*args, **kwargs)


class ContactUsForm(forms.ModelForm):
    """
    Add a Contact Us Form
    """
    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
