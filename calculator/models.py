from django.db import models

# Create your models here.
class Laptop(models.Model):
    Laptop_name=models.CharField(max_length=30)
    Laptop_desc=models.TextField()
    Laptop_img=models.FileField(upload_to="img/",max_length=250,null=True,default=None)