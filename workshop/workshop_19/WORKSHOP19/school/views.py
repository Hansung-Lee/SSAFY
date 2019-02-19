from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'school/index.html', {'students': students})
    
def create(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    
    Student.objects.create(name=name, email=email, birthday=birthday, age=age)
    return redirect('school:index')
    
def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('school:index')
    
def update(request, student_id):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    
    student = Student.objects.get(pk=student_id)
    student.name = name
    student.email = email
    student.birthday = birthday
    student.age = age
    
    student.save()
    
    return redirect('school:index')
    
def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'school/edit.html', {'student': student})