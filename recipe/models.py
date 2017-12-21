from django.db import models
from django.utils import timezone
from PIL import Image
from .choices import *

class Recipe(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    explanation = models.CharField(max_length=200, null=True)
    dietary = models.IntegerField(choices=DIETARY_CHOICES, default=1)
    vegetables = models.TextField(null=True, blank=True)
    meat = models.TextField(blank=True, null=True)
    recipe = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(blank=True, null=True, upload_to='images')
    seen = models.IntegerField(default =0, editable = False)
    def str(self):
        return self.title

    def increase(self):
        x = int(self.seen)
        x += 1
        self.seen = x
        self.save(update_fields=["seen"])
        return self.seen
