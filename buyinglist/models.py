from django.db import models
from django.utils import timezone
# Create your models here.


class Item(models.Model):
    name = models.CharField(default=None,max_length=50)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"
    
class List(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(default=None,max_length=50)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"

class User(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(default=None,max_length=50)
    last_name = models.CharField(default=None,max_length=50)
    email = models.EmailField(default=None)
    lists = models.ForeignKey(List,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
