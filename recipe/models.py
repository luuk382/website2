from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return self.title
