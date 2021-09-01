from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL


# Create your models here.
class Search(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    keyword = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.keyword)

