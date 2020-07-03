from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from test_restapi.serializers import librarySerializer, studentSerializer
from . models import library, student

# Create your views here.

class LibraryData(APIView):

	def get(self, request):
		queryset = library.objects.all()
		serializer = librarySerializer(queryset, many = True)
		return Response(serializer.data)

	def post(self):
		pass

class StudentData(APIView):

	def get(self, request):
		queryset = student.objects.all()
		serializer = studentSerializer(queryset, many = True)
		return Response(serializer.data)

	def post(self):
		pass