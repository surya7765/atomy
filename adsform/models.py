from django.db import models

# Create your models here.
class Message(models.Model):
    """docstring for Message."""
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
