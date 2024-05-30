from django.db import models
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    src = models.TextField()
    pub_date = models.DateTimeField('date published')
    views = models.PositiveIntegerField(default=0)  # Добавьте поле для просмотров
    def __str__(self):
        return str(self.title)
