from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(null=False, max_length=255)

class Assessment(models.Model):
    llm = models.CharField(max_length=255)
    datasetname = models.CharField(max_length=255)
    remark = models.FloatField(default=0.0)
