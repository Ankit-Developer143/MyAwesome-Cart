# Generated by Django 3.1.1 on 2020-09-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200919_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone1',
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
