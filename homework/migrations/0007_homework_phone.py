# Generated by Django 4.0.2 on 2022-03-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_homework_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
