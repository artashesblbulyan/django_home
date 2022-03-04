# Generated by Django 4.0.2 on 2022-03-04 21:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0007_homework_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]