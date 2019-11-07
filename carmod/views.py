from django.shortcuts import render, redirect

from .models import Car, Category, Part

from .forms import CarForm, CategoryForm, PartForm

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

def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'carmod/car_detail.html', {'car': car})

def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'carmod/category_detail.html', {'category': category})

def part_detail(request, pk):
    part = Part.objects.get(id=pk)
    return render(request, 'carmod/part_detail.html', {'part': part})

def car_create(request):
    if request.method == 'POST':
        #add new car to database
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        # if it's a get request, render form
        form = CarForm()
    return render(request, 'carmod/car_form.html', {'form': form})

def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'carmod/car_form.html', {'form': form})

def car_delete(request, pk):
    #car = Car.objects.get(pk=pk)
    Car.objects.get(id=pk).delete()
    return redirect('car_list')

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('car_detail', pk=category.car.pk)
    else:
        form = CategoryForm()
    return render(request, 'carmod/category_form.html', {'form': form})

def category_edit(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('car_detail', pk=category.car.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'carmod/category_form.html', {'form': form})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    Category.objects.get(id=pk).delete()
    return redirect('car_detail', pk=category.car.pk)

def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save()
            return redirect('part_detail', pk=part.pk)
    else:
        form = PartForm()
    return render(request, 'carmod/part_form.html', {'form': form})

def part_edit(request, pk):
    part = Part.objects.get(pk=pk)
    if request.method == "POST":
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            part = form.save()
            return redirect('part_detail', pk=part.pk)
    else:
        form = PartForm(instance=part)
    return render(request, 'carmod/part_form.html', {'form': form})

def part_delete(request, pk):
    part = Part.objects.get(pk=pk)
    Part.objects.get(id=pk).delete()
    return redirect('car_detail', pk=part.category.car.pk)