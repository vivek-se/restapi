from rest_framework import serializers
from . models import library, student


class librarySerializer(serializers.ModelSerializer):
	class Meta:
		model = library
		fields = '__all__'

class studentSerializer(serializers.ModelSerializer):
	class Meta:
		model = student
		fields = '__all__'