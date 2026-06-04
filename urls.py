from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls)
    # localhost:8000/         → myapp/urls.py
    path('', include('myapp.urls')),
]
