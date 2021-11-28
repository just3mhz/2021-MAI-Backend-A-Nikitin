from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    reg_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


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
