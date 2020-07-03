"""test_restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import StreamingHttpResponse
from rest_framework import routers
from test_restapi import views





urlpatterns = [
	path('library/', views.LibraryData.as_view()),
	path('library/<book_id>', views.LibraryDataid.as_view()),
	path('student/', views.StudentData.as_view()),
	path('student/<student_id>/', views.StudentDataid.as_view()),
	#path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('admin/', admin.site.urls),
]
