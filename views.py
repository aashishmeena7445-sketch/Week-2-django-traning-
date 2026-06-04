# myapp/views.py
# ─────────────────────────────────────────────
# VIEWS — Yahan logic hoti hai
# User request bhejta hai → View response deta hai
# ─────────────────────────────────────────────

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student, Subject


# ── VIEW 1: Home Page ─────────────────────────
# URL: localhost:8000/
def home(request):
    # Saare students database se lo
    students = Student.objects.all()
    total    = students.count()

    # Template ko data bhejo
    context = {
        'students': students,
        'total':    total,
    }
    return render(request, 'myapp/home.html', context)


# ── VIEW 2: Student Detail ────────────────────
# URL: localhost:8000/student/1/
def student_detail(request, pk):
    # pk se student dhoondho — nahi mila to 404
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'myapp/detail.html', {'student': student})


# ── VIEW 3: Student Add ───────────────────────
# URL: localhost:8000/add/
def student_add(request):
    if request.method == 'POST':
        # Form se data lo
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        subject = request.POST.get('subject')
        marks   = request.POST.get('marks', 0)

        # Database mein save karo
        Student.objects.create(
            name    = name,
            email   = email,
            subject = subject,
            marks   = int(marks),
        )
        # Home page pe bhejo
        return redirect('home')

    # GET request — form dikhao
    return render(request, 'myapp/add.html')


# ── VIEW 4: Student Delete ────────────────────
# URL: localhost:8000/delete/1/
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')


# ── VIEW 5: Simple Test View ──────────────────
# URL: localhost:8000/test/
# Sirf text return karta hai — template nahi
def test_view(request):
    return HttpResponse("<h1>Django Chal Raha Hai! ✅</h1>")
