from django.contrib import admin
from .models import Product, Roast, Size, CoffeeType

# Register your models here.
admin.site.register(Product)
admin.site.register(Roast)
admin.site.register(Size)
admin.site.register(CoffeeType)
