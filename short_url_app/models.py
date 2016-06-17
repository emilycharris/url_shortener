from django.contrib.auth.models import User
from django.db import models


# When a user uses a bookmark URL,
# record that bookmark and timestamp.
# A suggested name for this model is Click,
# even though you can navigate to the URL without a click by
# entering it in your navigation bar.


# Create your models here.
from django.utils import timezone


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    url = models.URLField()
    description = models.CharField(max_length=100)


class Click(models.Model):
    user = models.ForeignKey(User)
    url = models.ForeignKey(Bookmark)
    created = models.DateTimeField(auto_now_add=True)

