from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

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
    """Returns a string representation of a message."""
    date = timezone.localtime(self.log_date)
    return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Product(models.Model):
    title = models.CharField(
        max_length=40
    )  # allowing the admin to create a title for a new product
    group = models.CharField(max_length=15)  # either an instrument or an equipment
    description = models.TextField()
    pricing = models.DecimalField(max_digits=8, decimal_places=2)

    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])

    def __str__(self):
        return self.title

class Feedback(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Anonymous - {self.created_at.strftime('%Y-%m-%d')}"

