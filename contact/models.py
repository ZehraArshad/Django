from django.db import models

from django.db import models


class ContactSubmission(models.Model):
    message_name = models.CharField(max_length=100)
    message_email = models.EmailField()
    message = models.TextField()
    age = models.IntegerField(default=0)  #
    location = models.CharField(max_length=100, default="Karachi")  #
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_name


# Create your models here.
