from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    node0=models.CharField(max_length=1)
    node1=models.CharField(max_length=1)
    node2=models.CharField(max_length=1)
    node3=models.CharField(max_length=1)
    node4=models.CharField(max_length=1)
    node5=models.CharField(max_length=1)
    node6=models.CharField(max_length=1)
    node7=models.CharField(max_length=1)
    node8=models.CharField(max_length=1)
    