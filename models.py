from django.db import models
class Student(models.Model):

    # CharField  = chhota text (naam, email)
    name    = models.CharField(max_length=100)
    email   = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    # IntegerField = number
    marks   = models.IntegerField(default=0)

    # DateTimeField = date aur time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']   # Naya pehle


class Subject(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)   # TextField = lamba text

    def __str__(self):
        return self.name
