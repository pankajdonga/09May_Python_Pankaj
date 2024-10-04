# Generated by Django 5.0.7 on 2024-10-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_title', models.CharField(max_length=100)),
                ('event_img', models.ImageField(upload_to='profile_img')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]