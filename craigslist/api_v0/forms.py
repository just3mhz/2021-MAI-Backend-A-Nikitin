from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(label="Title", max_length=60)
    description = forms.CharField(label="Description", max_length=600)
    price = forms.IntegerField(label="Price")
    pub_date = forms.DateField(label="Publication date")
    published = forms.BooleanField(label="Published")

    category_id = forms.IntegerField(label="Category")
    user_id = forms.IntegerField(label="User")
