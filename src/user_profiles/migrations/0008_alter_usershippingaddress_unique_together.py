# Generated by Django 3.2.3 on 2022-12-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0007_auto_20221128_2035'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usershippingaddress',
            unique_together={('region', 'commune', 'address', 'user')},
        ),
    ]
