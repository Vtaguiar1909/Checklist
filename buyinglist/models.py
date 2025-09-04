from django.db import models
from django.utils import timezone
# Create your models here.

class Item(models.Model):
    name = models.CharField(default=None,max_length=50)
    quantity = models.IntegerField(default=1)
    type_product = models.CharField(default=None,max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"