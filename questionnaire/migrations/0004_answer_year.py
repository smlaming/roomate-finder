# Generated by Django 3.1.7 on 2021-03-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='year',
            field=models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th')], default='1st', max_length=50),
        ),
    ]
