from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.

VISIBILITY_CHOICE = (
    ("public", "public"),
    ("private", "private"),
    ("friends", "friends"),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(choices=VISIBILITY_CHOICE, max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=3000)
    image = models.ImageField(upload_to="images/", blank=True)
    likes = models.IntegerField()
    comments = models.CharField(max_length=3000)
    shares = models.IntegerField()

    def get_comments(self):
        return json.loads(self.comments)

    def set_comments(self, x):
        self.comments = json.dumps(x)

    def __str__(self):
        return f"{self.user.username} {self.date_created}"
