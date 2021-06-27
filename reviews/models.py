from django.db import models
from django.db.models.constraints import CheckConstraint
from django.db.models.deletion import CASCADE
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communcation = models.IntegerField()
    cleanlines = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room.name}-{self.user.username}-{self.review}"

    pass
