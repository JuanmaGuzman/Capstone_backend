# Generated by Django 3.2.3 on 2022-11-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20221102_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('discount', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
