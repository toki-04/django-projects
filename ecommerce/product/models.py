from django.db import models

# Create your models here.

ROAST_CHOICES = (
    ("light", "light"),
    ("medium", "medium"),
    ("dark", "dark"),
)

SIZE_CHOICE = (
    ("12", "12oz"),
    ("16", "16oz"),
    ("32", "32oz"),

)

COFFEE_TYPE_CHOICE = (
    ("decaf", "decaffeinated"),
    ("easy-late", "easy-late"),
    ("flavored", "flavored"),
    ("ground", "ground"),
    ("organic", "organic"),
    ("reserved", "reserved"),
    ("seasonal", "seasonal"),
    ("whole-bean", "whole bean"),
)


class Roast(models.Model):
    roast = models.CharField(choices=ROAST_CHOICES, max_length=20)

    def __str__(self):
        return self.roast


class Size(models.Model):
    size = models.CharField(choices=SIZE_CHOICE, max_length=3)

    def __str__(self):
        return self.size


class CoffeeType(models.Model):
    coffee_type = models.CharField(choices=COFFEE_TYPE_CHOICE, max_length=20)

    def __str__(self):
        return self.coffee_type


class Product(models.Model):
    name = models.CharField(max_length=100)
    roast = models.ManyToManyField(Roast)
    size = models.ManyToManyField(Size)
    coffee_type = models.ManyToManyField(CoffeeType)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
