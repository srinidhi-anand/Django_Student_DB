from django.db import connections
from django.db import models

class Student(models.Model): 
	Id = models.CharField(max_length=100)
	Name = models.CharField(max_length=100)
	Roll_No = models.CharField(max_length=100)
	College = models.CharField(max_length=100)
	class Meta:
		db_table = "student_db"


class Course(models.Model): 
	Id = models.CharField(max_length=100)
	Course = models.CharField(max_length=100)	
	Student_id = models.CharField(max_length=100)
	Academic_year = models.CharField(max_length=100)
	Semester = models.CharField(max_length=100)
	Marks = models.CharField(max_length=100)
	class Meta:
		db_table = "course_db"
		
class Sem_2(models.Model): 
	Id = models.CharField(max_length=100)
	Course = models.CharField(max_length=100)	
	Student_id = models.CharField(max_length=100)
	Academic_year = models.CharField(max_length=100)
	Semester = models.CharField(max_length=100)
	Par_course = models.CharField(max_length=100)
	Marks = models.CharField(max_length=100)
	class Meta:
		db_table = "tp_sem_2"
		
		
class Sem_3(models.Model): 
	Id = models.CharField(max_length=100)
	Course = models.CharField(max_length=100)	
	Student_id = models.CharField(max_length=100)
	Academic_year = models.CharField(max_length=100)
	Semester = models.CharField(max_length=100)
	Par_course = models.CharField(max_length=100)
	Marks = models.CharField(max_length=100)
	class Meta:
		db_table = "tp_sem_3"
		
class Sem_4(models.Model): 
	Id = models.CharField(max_length=100)
	Course = models.CharField(max_length=100)	
	Student_id = models.CharField(max_length=100)
	Academic_year = models.CharField(max_length=100)
	Semester = models.CharField(max_length=100)
	Par_course = models.CharField(max_length=100)
	Marks = models.CharField(max_length=100)
	class Meta:
		db_table = "tp_sem_4"
