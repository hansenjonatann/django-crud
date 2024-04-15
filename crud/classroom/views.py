from django.shortcuts import render , redirect
from .models import Student

# Create your views here.

def index(request):
  student=Student.objects.all()
  return render(request=request, template_name='index.html', context={"students" : student})

def add(request):
  return render(request=request , template_name='add.html' )

def addValue(request):
  nama_field = request.POST['nama']
  kelas_field = request.POST['kelas']
  student = Student(nama = nama_field , kelas = kelas_field)
  student.save()
  return redirect('/')

def delete(request,id):
  student = Student.objects.get(id=id)
  student.delete()
  return redirect('/')

def update(request,id):
  student = Student.objects.get(id=id)
  return render(request=request , template_name='update.html' , context={'stu' : student})

def updateValue(request, id):
  nama_field = request.POST['nama']
  kelas_field = request.POST['kelas']
  stu = Student.objects.get(id=id)
  stu.nama = nama_field
  stu.kelas = kelas_field
  stu.save()
  return redirect('/')