from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Sum
from stud_app.models import Student, Course, Sem_3, Sem_2, Sem_4

# Create your views here.

def show(request):
	students = Student.objects.all()
	list_of_sem = [2,3,4]
	return render(request,"stud_table.html",{'student':students ,'sem_list': list_of_sem })


def view_detail(request, key_id, sem_id):
	text =" The student number is %s." %key_id
	students = Student.objects.get(Id=int(key_id))
	Ovr_mrks = Course.objects.filter(Student_id=int(key_id), Semester=int(sem_id)).aggregate(sum=Sum('Marks')/ 6)['sum']
	course = Course.objects.filter(Student_id=int(key_id), Semester=int(sem_id)).order_by('id')
	if sem_id in [2,3,4]:
		S = Sem_2.objects.filter(Student_id=int(key_id)).order_by('Par_course') if int(sem_id) == 2 else (  Sem_3.objects.filter(Student_id=int(key_id)).order_by('Par_course') if int(sem_id) == 3 else Sem_4.objects.filter(Student_id=int(key_id)).order_by('Par_course') )
	else:
		S=''
	return render(request,"detail.html",{'student':students,'course':course,'Test_paper':S,'sem_id':sem_id,'Ovr_mrks':Ovr_mrks})
