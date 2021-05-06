# Generated by Django 3.1.6 on 2021-05-06 01:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20210420_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ideal_rent',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(200, message='Please enter a number above 200'), django.core.validators.MaxValueValidator(1500, message='Please enter a number below 1500')]),
        ),
    ]
