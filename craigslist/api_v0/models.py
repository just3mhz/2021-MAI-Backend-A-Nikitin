from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    reg_date = models.DateField()


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)

    category = models.CharField(max_length=60)


class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.IntegerField()
    description = models.CharField(max_length=600)
    pub_date = models.DateField()
    published = models.BooleanField(default=False)
