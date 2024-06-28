from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "profile",
            "visibility",
            "date_created",
            "text",
            "image",
            "likes",
            "comments",
            "shares",
        )

    def get_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")
