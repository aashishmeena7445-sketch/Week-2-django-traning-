from django.urls import path
from . import views   

urlpatterns = [

    # localhost:8000/          → home view
    path('', views.home, name='home'),

    # localhost:8000/test/     → test view
    path('test/', views.test_view, name='test'),

    # localhost:8000/add/      → student add form
    path('add/', views.student_add, name='student-add'),

    # localhost:8000/student/1/ → student detail
    path('student/<int:pk>/', views.student_detail, name='student-detail'),

    # localhost:8000/delete/1/ → student
    path('delete/<int:pk>/', views.student_delete, name='student-delete'),
]
