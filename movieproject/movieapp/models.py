from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    m_desc = models.TextField(default='none')
    img = models.ImageField(upload_to='poster', default='null')
