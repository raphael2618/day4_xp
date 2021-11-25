from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()


class Todo(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    hasBeenDone = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True)
    deadline_date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
