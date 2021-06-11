from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        
class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields = '__all__'

class BirthSerislizer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=100)
    Gender = serializers.CharField(max_length=10)
    Marital_Status = serializers.CharField(max_length=15)
    Date_of_birth = serializers.DateField()
    Time = serializers.TimeField()
    Country_of_birth = serializers.CharField(max_length=100)
    State_of_birth = serializers.CharField(max_length=100)
    Place_of_birth = serializers.CharField(max_length=100)
    Longitude = serializers.CharField(max_length=100)
    Latitude = serializers.CharField(max_length=100)

    class Meta:
        model = Birth
        fields = '__all__'

class ContactDetailSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(max_length=200)
    Mobile = serializers.CharField(max_length=20)
    Address = serializers.CharField(max_length=150)
    Question = serializers.CharField(max_length=1000)

    class Meta:
        model = ContactDetail
        fields = '__all__'