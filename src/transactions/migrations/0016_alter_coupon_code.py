# Generated by Django 3.2.3 on 2022-12-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_acountlesstransaction_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
