# Generated by Django 5.1.1 on 2024-11-14 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart_order',
        ),
    ]