from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(default = '', max_length = 100)

    def __str__(self):
        return self.name

class Part(models.Model):
    part_name = models.CharField(default = '', max_length = 100)
    part_num = models.CharField(default = '', max_length = 100)
    quantity = models.PositiveIntegerField(default='0')
    price_each = models.DecimalField(default='0.00', max_digits=8, decimal_places=2)
    price_total = models.DecimalField(default='0.00', max_digits=8, decimal_places=2)
    link_part = models.TextField(default="")
    notes = models.CharField(default = '', max_length = 500)
    image_url = models.CharField(default = '', max_length = 512)
    installed = models.BooleanField(default=False)
    models.ForeignKey(Category, on_delete = 'CASCADE', related_name = 'parts')

