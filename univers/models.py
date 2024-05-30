from django.db import models

class Univers(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos_news/')
    content = models.TextField()
    src = models.TextField()
    Management = models.CharField(max_length=200 , verbose_name ='Руководство')
    start_date = models.CharField(max_length=200 , verbose_name ='Год основания')
    site = models.CharField(max_length=200 , verbose_name ='Сайт')
    email = models.CharField(max_length=200 , verbose_name ='E-mail')
    karta = models.TextField()
    views = models.PositiveIntegerField(default=0)  # Добавьте поле для просмотров
    def __str__(self):
        return str(self.title)