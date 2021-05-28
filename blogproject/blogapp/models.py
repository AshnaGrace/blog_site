from django.db import models

# Create your models here.
class news(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    # sub=models.TextField()
    desc=models.TextField()
    month=models.CharField(max_length=100)
    date=models.IntegerField()