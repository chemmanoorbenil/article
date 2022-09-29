from django.db import models


# Create your models here.
class Art(models.Model):
    title=models.CharField(max_length=200)
    auther=models.CharField(max_length=100)
    emil=models.EmailField(max_length=200)
    date=models.DateField(max_length=200)
    
    def __str__(self):
        return self.title
