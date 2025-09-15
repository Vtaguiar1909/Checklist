from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name = models.CharField(default=None,max_length=50)
    quantity = models.IntegerField(default=1)
    type_product = models.CharField(default=None,max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"