# myapp/models.py
# ─────────────────────────────────────────────
# DATABASE MODELS
# Har model = database mein ek table
# ─────────────────────────────────────────────

from django.db import models


# ── MODEL 1: Student ──────────────────────────
# yeh table students ki info store karegi
class Student(models.Model):

    # CharField  = chhota text (naam, email)
    name    = models.CharField(max_length=100)
    email   = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    # IntegerField = number
    marks   = models.IntegerField(default=0)

    # DateTimeField = date aur time
    created_at = models.DateTimeField(auto_now_add=True)

    # Admin panel mein naam dikhayega
    def __str__(self):
        return self.name

    # Table ka naam aur sorting
    class Meta:
        ordering = ['-created_at']   # Naya pehle


# ── MODEL 2: Subject ─────────────────────────
# subjects ki list
class Subject(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)   # TextField = lamba text

    def __str__(self):
        return self.name
