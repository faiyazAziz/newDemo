from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now_add=False)
    pages = models.IntegerField()
    
