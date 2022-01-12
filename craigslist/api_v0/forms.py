from django import forms
from django.core.files import images

from .models import User
from .models import Category
from .models import Advertisement


class AdvertisementForm(forms.Form):
    title = forms.CharField(label="Title", max_length=60)
    description = forms.CharField(label="Description", max_length=600)
    price = forms.IntegerField(label="Price")
    pub_date = forms.DateField(label="Publication date")
    published = forms.BooleanField(label="Published")
    category = forms.ModelChoiceField(Category.objects.all(), label="User")
    user = forms.ModelChoiceField(User.objects.all(), label="Category")


class UserUploadPhotoForm(forms.Form):
    upload_photo = forms.ImageField(label='Select image')

    def clean_upload_photo(self):
        upload_photo = self.cleaned_data['upload_photo']

        try:
            w, h = images.get_image_dimensions(upload_photo)
            max_width = max_height = 300

            if w > max_width and h > max_height:
                raise forms.ValidationError(f'Please use images at most {max_width}x{max_height} pixels.')

            main, sub = upload_photo.content_type.split('/')
            if main != 'image' or sub not in ['jpeg', 'gif', 'png']:
                raise forms.ValidationError(f'Please use JPEG, GIF or PNG images')
        except AttributeError:
            pass

        return upload_photo


class CommentForm(forms.Form):
    comment = forms.CharField(label="Comment Message", max_length=1000)

