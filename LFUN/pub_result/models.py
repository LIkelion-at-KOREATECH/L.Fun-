from django.db import models

# Create your models here.

class Result(models.Model):
    result_url1 = models.CharField(max_length=300)
    result_url2 = models.CharField(max_length = 100)