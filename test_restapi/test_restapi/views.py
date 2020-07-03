from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from test_restapi.serializers import librarySerializer, studentSerializer
from . models import library, student
#from rest_framework.permissions import IsAuthenticated

# Create your views here.

class LibraryData(APIView):
	#permission_classes = (permissions.AllowAny,)
	#permission_classes = [IsAuthenticated]

	def get(self, request):
		queryset = library.objects.all()
		serializer = librarySerializer(queryset, many = True)
		return Response(serializer.data)

	def post(self, request):
		data = request.data
		obj=library.objects.create(book_id = data[0],book_name = data[1], student_id = data[2])
		obj.save()


class LibraryDataid(APIView):

	def get(self, request, book_id):
		queryset = library.objects.filter(book_id = book_id)
		serializer = librarySerializer(queryset, many = True)
		return Response(serializer.data)




class StudentData(APIView):

	def get(self, request):
		queryset = student.objects.all()
		serializer = studentSerializer(queryset, many = True)
		return Response(serializer.data)

	def post(self):
		pass


class StudentDataid(APIView):

	def get(self, request, student_id):
		queryset = student.objects.filter(student_id = student_id)
		serializer = studentSerializer(queryset, many = True)
		return Response(serializer.data)

	def post(self):
		pass