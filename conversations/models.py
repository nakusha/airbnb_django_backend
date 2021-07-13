import conversations
from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        username = []
        for user in self.participants.all():
            username.append(user.username)
        return ", ".join(username)

    def count_message(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

    count_message.short_description = "Number of Message"
    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    """Message Model Definitions"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}: {self.message}"
