# Generated by Django 2.2.7 on 2019-11-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmod', '0002_auto_20191106_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='car',
            field=models.ForeignKey(default='', on_delete='CASCADE', related_name='parts', to='carmod.Car'),
        ),
        migrations.AlterField(
            model_name='part',
            name='category',
            field=models.ForeignKey(default='', on_delete='CASCADE', related_name='parts', to='carmod.Category'),
        ),
    ]
