# Generated by Django 3.2 on 2021-04-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restasite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
    ]
