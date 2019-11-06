from django.shortcuts import render, redirect

from .models import Car, Category, Part

# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    return render(request, "carmod/car_list.html", {"cars": cars})

def category_list(request):
    categorys = Category.objects.all()
    return render(request, "carmod/category_list.html", {"categorys": categorys})

def part_list(request):
    parts = Part.objects.all()
    return render(request, "carmod/part_list.html", {"parts": parts})