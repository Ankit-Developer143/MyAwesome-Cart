# Generated by Django 3.1.1 on 2020-09-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default='', max_length=70),
        ),
    ]