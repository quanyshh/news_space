from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='photos_news/')
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # Добавьте поле для просмотров
    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField('date publish',auto_now_add=True)
    def __str__(self):
        return str(self.post)
