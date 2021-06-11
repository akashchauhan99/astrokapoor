from django.http.response import Http404
from django.shortcuts import render
from .serializers import *
from ..models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class SellerView(APIView):
    def get(self, request):
        seller = Seller.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)
    
class CategoryServiceView(APIView):
    def get_object(self, pk):
        try:
            return CategoryService.objects.get(pk=pk)
        except CategoryService.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        categorySerivice = self.get_object(pk)
        serializer = CategoryServiceSerializer(categorySerivice)
        return Response(serializer.data)

class BirthView(APIView):
    def get(self, request):
        birth = Birth.objects.all()
        serializer = BirthSerislizer(birth, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = BirthSerislizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BirthDetailView(APIView):
    def get_object(self, pk):
        try:
            return Birth.objects.get(pk=pk)
        except Birth.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        birthdetail = self.get_object(pk)
        serializer = BirthSerislizer(birthdetail)
        return Response(serializer.data)

    def put(self, request, pk):
        birthdetail = self.get_object(pk)
        serializer = BirthSerislizer(birthdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        birthdetail = self.get_object(pk)
        birthdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ContactView(APIView):
    def get(self, request):
        contactdetail = ContactDetail.objects.all()
        serializer = ContactDetailSerializer(contactdetail, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = ContactDetailSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetailView(APIView):
    def get_object(self, pk):
        try:
            return ContactDetail.objects.get(pk=pk)
        except ContactDetail.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        contactdetail = self.get_object(pk)
        serializer = ContactDetailSerializer(contactdetail)
        return Response(serializer.data)

    def put(self, request, pk):
        contactdetail = self.get_object(pk)
        serializer = ContactDetailSerializer(contactdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        contactdetail = self.get_object(pk)
        contactdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)