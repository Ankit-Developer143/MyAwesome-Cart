# Generated by Django 3.1.1 on 2020-09-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]