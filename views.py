
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student, Subject


# ── VIEW 1: Home Pagg
# URL: localhost:8000/
def home(request):
    students = Student.objects.all()
    total    = students.count()
    context = {
        'students': students,
        'total':    total,
    }
    return render(request, 'myapp/home.html', context)


# ── VIEW 2: Student Detail
# URL: localhost:8000/student/1/
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'myapp/detail.html', {'student': student})


# ── VIEW 3: Student Add ──
# URL: localhost:8000/add/
def student_add(request):
    if request.method == 'POST':
        # Form se data lo
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        subject = request.POST.get('subject')
        marks   = request.POST.get('marks', 0)
        Student.objects.create(
            name    = name,
            email   = email,
            subject = subject,
            marks   = int(marks),
        )
        return redirect('home')

    # GET request 
    return render(request, 'myapp/add.html')


# ── VIEW 4: Student Delete ──
# URL: localhost:8000/delete/1/
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')


# ── VIEW 5: Simple Test View 
# URL: localhost:8000/test/
def test_view(request):
    return HttpResponse("<h1>Django Chal Raha Hai! ✅</h1>")
