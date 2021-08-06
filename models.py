from django.db import models
from django.urls import reverse

# Create your models here.

import uuid

class Album(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('photo', args=[str(self.id)])

    class Meta:
        ordering = ['-uploaded']
