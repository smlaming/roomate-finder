# Generated by Django 3.1.5 on 2021-04-02 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0007_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='go_to_bed',
            field=models.CharField(choices=[('1', 'Before 9pm'), ('2', '9pm-10:30pm'), ('3', '10:30pm-12:00am'), ('4', '12:00am-1:30am'), ('5', 'After 1:30am')], max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='guests',
            field=models.CharField(choices=[('1', 'Always love to have guests over'), ('2', 'Usually love to have guests over'), ('3', 'Sometimes love to have guests over'), ('4', 'Never love to have guests over')], max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='how_clean',
            field=models.CharField(choices=[('1', 'Very Clean'), ('2', 'Kinda Clean'), ('3', 'Kinda Messy'), ('4', 'Very Messy')], max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='ideal_rent',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='more_introverted_or_extroverted',
            field=models.CharField(choices=[('1', 'Introverted'), ('2', 'Extroverted'), ('3', 'In the middle')], max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='wake_up',
            field=models.CharField(choices=[('1', 'Before 7am'), ('2', '7am-8:30am'), ('3', '8:30am-10am'), ('4', '10am-11:30am'), ('5', 'After 11:30am')], max_length=200),
        ),
    ]
