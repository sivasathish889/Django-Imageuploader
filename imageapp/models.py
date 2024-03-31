from django.db import models

# Create your models here.
class Imagemodel(models.Model):
    title=models.CharField(max_length=80,default="")
    image= models.ImageField(
        upload_to="myimage",
        null=False,
        blank=False, 
        )
    date=models.DateTimeField(auto_now_add=True)
    

