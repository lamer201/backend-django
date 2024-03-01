from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.TextField()
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    max_user = models.IntegerField('Максимально учеников')
    min_user = models.IntegerField('Минимально учеников')
    users = models.ManyToManyField(User, blank=True)


class Learn(models.Model):
    name = models.TextField()
    url_video = models.URLField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='learns')
    

class Group(models.Model):
    name = models.TextField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='groups')
    users = models.ManyToManyField(User, blank=True)


class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
