# myproject/urls.py
# ─────────────────────────────────────────────
# Main URL Configuration
# Yahan se saari URLs alag apps ko bhejti hain
# ─────────────────────────────────────────────

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Hamari app ki saari URLs
    # localhost:8000/         → myapp/urls.py
    path('', include('myapp.urls')),
]
