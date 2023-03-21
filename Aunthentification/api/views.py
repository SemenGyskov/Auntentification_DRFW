from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializer import *

class ClassCreate(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminUser,)
class ClassList(APIView):
    def get(self,request):
        w = Class.objects.all()
        return Response({'classes':ClassSerializer(w,many=True).data})
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ClassAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminUser,)

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)

class StudentList(APIView):
    def get(self, request):
        w = Student.objects.all()
        return Response({'students': StudentSerializer(w, many=True).data})
    permission_classes = (IsAuthenticatedOrReadOnly,)

class StudentAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)

class ItemCreate(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ItemList(APIView):
    def get(self, request):
        w = Item.objects.all()
        return Response({'Items': ItemSerializer(w, many=True).data})
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ItemAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAdminUser,)

