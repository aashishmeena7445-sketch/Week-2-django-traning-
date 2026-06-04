from django.contrib import admin
from .models import Student, Subject

admin.site.register(Subject)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'subject', 'marks', 'created_at']
    list_filter   = ['subject']

    search_fields = ['name', 'email']
