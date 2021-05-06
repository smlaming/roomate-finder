# Generated by Django 3.1.6 on 2021-05-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_auto_20210505_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.FloatField(choices=[('1', '0.25'), ('2', '0.5'), ('3', '0.75'), ('4', '1.0')], default=1.0, help_text='Duration of meeting in hours'),
        ),
    ]
