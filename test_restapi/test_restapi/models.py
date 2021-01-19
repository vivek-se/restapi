from django.db import models
from django.db.models.signals import post_save

class student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	book_id = models.IntegerField()
	

class library(models.Model):
	book_id = models.IntegerField(primary_key=True)
	book_name = models.CharField(max_length=100)
	student_id = models.ForeignKey(student, on_delete=models.CASCADE)


def student_save(sender, instance, **kwargs):
	 print("New student saved")
	 sobject = student.objects.latest('student_id')
	 bid = getattr(sobject, 'book_id')
	 obj=library.objects.create(book_id = bid, student_id = sobject)
	 obj.save()

#for signal
post_save.connect(student_save, sender = student)
 
