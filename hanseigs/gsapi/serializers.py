from rest_framework import serializers
from .models import Mealdata

class Mealdataserializer(serializers.ModelSerializer):
    class Meta:
        model = Mealdata
        fields = ('date_data','meal_data')
