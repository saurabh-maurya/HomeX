from rest_framework import serializers
from .models import ApplianceStatus
from django.contrib.auth.models import User

class ApplianceStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApplianceStatus
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','password','email','first_name')