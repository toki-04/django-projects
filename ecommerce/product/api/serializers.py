from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "roast",
            "size",
            "coffee_type",
            "price",
            "created",
        )

    def get_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")
