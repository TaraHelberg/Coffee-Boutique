from django import forms
from .models import ContactUs


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
