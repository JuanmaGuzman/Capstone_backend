# Generated by Django 3.2.3 on 2022-11-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0016_auto_20221124_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
