
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tags = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' - ' + self.username + ' - ' + self.password

class Notes(models.Model):
    note_id = models.IntegerField()
    author_id = models.IntegerField()
    type = models.IntegerField()
    title = models.CharField(max_length=5000)
    tag = models.CharField(max_length=1000)
    content = models.CharField(max_length=60000)