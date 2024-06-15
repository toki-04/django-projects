from rest_framework import serializers
from ..models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = (
            "id",
            "name",
            "roast",
            "size",
            "quantity",
            "price",
            "image_url",
            "created_by",
        )

    def get_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")
