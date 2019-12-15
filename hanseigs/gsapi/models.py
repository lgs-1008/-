from django.db import models

# Create your models here.
class Mealdata(models.Model):
    date_data = models.IntegerField(primary_key=True, default = 0)
    meal_data = models.CharField(max_length=150, null = True)

    def __str__(self):
        return str(self.date_data)
