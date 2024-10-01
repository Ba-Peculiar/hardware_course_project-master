from django.db import models
from django.utils import timezone

# Create your models here.
class Temperature(models.Model):
    temperature = models.FloatField(default=0.00)
    humidity = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Temperatuture: {self.temperature}"
    