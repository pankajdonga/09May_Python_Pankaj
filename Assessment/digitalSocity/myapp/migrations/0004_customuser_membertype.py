# Generated by Django 5.0.7 on 2024-09-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_customuser_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='membertype',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]