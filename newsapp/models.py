from django.db import models

# Create your models here.
class createNews(models.Model):
    newsId = models.IntegerField(primary_key= True)
    title = models.CharField(max_length=100)
    newsDetails = models.TextField()
    coverImage = models.ImageField(upload_to='media')


#class updateNews(models.Model):
