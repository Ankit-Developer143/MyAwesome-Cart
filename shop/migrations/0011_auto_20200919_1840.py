# Generated by Django 3.1.1 on 2020-09-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200919_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
        migrations.AddField(
            model_name='orders',
            name='phone1',
            field=models.IntegerField(default='', max_length=20),
        ),
    ]