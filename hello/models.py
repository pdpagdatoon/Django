from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} – {self.created_at:%Y-%m-%d %H:%M}"


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")


def __str__(self):
    """Returns a string representation of a message."""
    date = timezone.localtime(self.log_date)
    return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
