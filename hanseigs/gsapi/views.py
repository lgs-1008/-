from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Mealdataserializer
from .models import Mealdata
# Create your views here.
class MealdataViewSet(viewsets.ModelViewSet):
    queryset = Mealdata.objects.all()
    serializer_class = Mealdataserializer
