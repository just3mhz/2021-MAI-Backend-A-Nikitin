from os import path

from django.db import models
from django.contrib.auth.models import AbstractUser


def upload_path(instance, filename):
    return path.join('users', instance.username, filename)


class User(AbstractUser):
    advertisements = models.IntegerField(default=0)
    profile_image = models.ImageField(
        null=True, upload_to=upload_path)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)

    category = models.CharField(max_length=60)

    def __str__(self):
        return self.category


class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.IntegerField()
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=600)
    pub_date = models.DateField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f'#{self.advertisement.advertisement_id}-{self.comment_id}: {self.comment}'
