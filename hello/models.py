from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} – {self.created_at:%Y-%m-%d %H:%M}"

class Comment(models.Model):
    page_identifier = models.CharField(max_length=255)  # stores request.path
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name} on {self.page_identifier}"