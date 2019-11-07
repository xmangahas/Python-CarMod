from django import forms
from .models import Car, Category, Part

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'car_model', 'trim', 'year')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'car')

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('part_name', 'part_num', 'quantity', 'price_each', 'price_total', 'link_part', 'notes', 'image_url', 'installed', 'category', 'car')