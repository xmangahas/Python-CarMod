# Generated by Django 2.2.7 on 2019-11-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmod', '0012_auto_20191107_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=8),
        ),
    ]
