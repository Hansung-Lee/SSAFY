from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
def student(request, name):
    age=28
    return render(request, 'student.html', {'name': name, 'age': age})