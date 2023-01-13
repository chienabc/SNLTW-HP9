from django.db import models

# Create your models here.
class listItem (models.Model):
    name = models.CharField(max_length=255 , null=False)
    price = models.FloatField(null=True)
    amount = models.IntegerField(null=True)
  
    
class About (models.Model):
     aboutme = models.CharField(max_length=255 , null=False)

def __str__(self):
    return f"{self.name} , {self.price} , {self.amount}, {self.aboutme}"

