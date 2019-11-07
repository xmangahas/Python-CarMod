from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(default = '', max_length = 100)
    car_model = models.CharField(default = '', max_length = 100)
    trim = models.CharField(default = '', max_length = 100)
    year = models.CharField(default = '', max_length=4)
    image_url = models.CharField(default = '', blank=True, max_length = 512)
    
    def __str__(self):
        return f"{self.year} - {self.make} - {self.car_model}"

class Category(models.Model):
    name = models.CharField(default = '', max_length = 100)
    car = models.ForeignKey(Car, default = '', on_delete = 'CASCADE', related_name = 'categorys')

    def __str__(self):
        return f"{self.name} for {self.car.car_model}"

class Part(models.Model):
    part_name = models.CharField(default = '', max_length = 100)
    part_num = models.CharField(default = '', max_length = 100)
    quantity = models.PositiveIntegerField(default='0')
    price_each = models.DecimalField(default='0.00', max_digits=8, decimal_places=2)
    price_total = models.DecimalField(default='0.00', blank=True, max_digits=8, decimal_places=2)
    link_part = models.CharField(default = '', max_length = 512)
    notes = models.TextField(default="", blank=True)
    image_url = models.CharField(default = '', blank=True, max_length = 512)
    installed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default = '', on_delete = 'CASCADE', related_name = 'parts')

    def __str__(self):
        return self.part_name

    @property
    def get_total_price(self):
        return self.quantity*self.price_each