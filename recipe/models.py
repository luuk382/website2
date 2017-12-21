from django.db import models
from django.utils import timezone
from PIL import Image

class Recipe(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
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
