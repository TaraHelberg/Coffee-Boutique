from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """Admin Add product form. Code from Boutique Ado"""

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('favourites',)

        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """Review & Rating Form"""
    class Meta:
        """Form model and Fields"""
        model = Review
        fields = ['review', 'rating']
