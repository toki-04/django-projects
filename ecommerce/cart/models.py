from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cart(models.Model):
    name = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.roast} {self.size} {self.quantity} {self.price}"
