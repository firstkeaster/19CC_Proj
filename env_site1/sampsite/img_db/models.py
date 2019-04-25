from django.db import models

## Create a image table
class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    ## upload_to: the folder name to store
    ## the images. will automatically create
    ## the folder after upload.
    name = models.CharField(max_length=20)


# Create your models here.
