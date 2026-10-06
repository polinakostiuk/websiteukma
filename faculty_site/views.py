from django.shortcuts import render, get_object_or_404
from .models import Department, MainPage, Specialty, ExchangeProgram

def index(request):
    info = MainPage.objects.first()
    return render(request, 'faculty_site/index.html', {'info': info})

def specialty_list(request):
    specialties = Specialty.objects.all()
    return render(request, 'faculty_site/programs.html', {'specialties': specialties})

def specialty_detail(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    courses_list = [c.strip() for c in specialty.courses.split('\n') if c.strip()]
    return render(request, 'faculty_site/program_detail.html', {
        'specialty': specialty,
        'courses_list': courses_list
    })

def department_list(request):
    departments = Department.objects.prefetch_related('graduating_specialties').all()
    return render(request, 'faculty_site/departments.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = department.teachers.all()
    return render(request, 'faculty_site/department_detail.html', {
        'department': department,
        'teachers': teachers
    })
def exchange_list(request):
    programs = ExchangeProgram.objects.order_by("deadline")
    return render(request, 'faculty_site/exchange.html', {'programs': programs})


