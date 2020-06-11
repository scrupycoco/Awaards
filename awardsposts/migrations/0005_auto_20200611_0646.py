# Generated by Django 3.0.7 on 2020-06-11 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awardsposts', '0004_auto_20200608_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='comment',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
