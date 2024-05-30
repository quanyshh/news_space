from django.db import models

class Gallarey(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos_news/')
    def __str__(self):
        return str(self.title)