from django.db import models

class student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	book_id = models.IntegerField()
	

class library(models.Model):
	book_id = models.IntegerField(primary_key=True)
	book_name = models.CharField(max_length=100)
	student_id = models.ForeignKey(student, on_delete=models.CASCADE)

	