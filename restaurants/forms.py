from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'opening_time', 'closing_time']

# name = models.CharField(max_length=120)
#     description = models.TextField()
#     opening_time = models.TimeField()
#     closing_time = models.TimeField()
