from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Products, Categories
from .serializers import ProductsSerializer

class GoodsAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class GoodsAPIUpdate(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    

class GoodsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly, )


