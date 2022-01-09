# Generated by Django 4.0 on 2022-01-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_address_profile_birthday_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Prefer Not To Say'), ('4', 'Other')], default=1, null=True),
        ),
    ]