# Generated by Django 3.0.7 on 2020-06-07 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsposts', '0002_auto_20200607_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='design_rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='usability_rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
