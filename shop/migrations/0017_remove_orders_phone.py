# Generated by Django 3.1.1 on 2020-09-19 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200919_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
    ]