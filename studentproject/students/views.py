from django.shortcuts import render,redirect
from .models import Student

# Read
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

# Create
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        
        Student.objects.create(name=name, email=email, course = course)
        return redirect('home')
    return render(request, 'add.html')

#update
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('home')
    return render(request, 'update.html', {'student':student})


# delete 
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')
