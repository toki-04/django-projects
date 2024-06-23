from django.db import models
from django.contrib.auth.models import User
# from community.models import Post

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="images/profile/", blank=True)
    followers = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True,
    )
    # posts = models.ManyToManyField(
    # Post,
    # symmetrical=False,
    # blank=True,
    # )

    def __str__(self):
        return self.user.username
