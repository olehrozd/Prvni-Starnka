# Generated by Django 4.2.2 on 2023-07-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_car_delete_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ImageField(upload_to='main/images/'),
        ),
    ]
