from django import forms

from .models import User
from .models import Category


class AdvertisementForm(forms.Form):
    title = forms.CharField(label="Title", max_length=60)
    description = forms.CharField(label="Description", max_length=600)
    price = forms.IntegerField(label="Price")
    pub_date = forms.DateField(label="Publication date")
    published = forms.BooleanField(label="Published")
    category = forms.ModelChoiceField(Category.objects.all(), label="User")
    user = forms.ModelChoiceField(User.objects.all(), label="Category")
