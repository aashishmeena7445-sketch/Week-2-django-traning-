# myapp/admin.py
# ─────────────────────────────────────────────
# ADMIN PANEL
# Yahan models register karo — admin mein dikhenge
# ─────────────────────────────────────────────

from django.contrib import admin
from .models import Student, Subject


# Simple registration
admin.site.register(Subject)

# Custom admin — zyada features ke saath
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Admin mein yeh columns dikhao
    list_display  = ['name', 'email', 'subject', 'marks', 'created_at']

    # Filter options (right side)
    list_filter   = ['subject']

    # Search box
    search_fields = ['name', 'email']
