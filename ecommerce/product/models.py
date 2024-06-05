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


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    roast = models.CharField(choices=ROAST_CHOICES, max_length=20)
    size = models.CharField(choices=SIZE_CHOICE, max_length=3)
    coffee_type = models.CharField(choices=COFFEE_TYPE_CHOICE, max_length=20)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
