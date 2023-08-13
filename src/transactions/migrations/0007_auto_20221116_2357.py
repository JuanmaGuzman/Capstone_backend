# Generated by Django 3.2.3 on 2022-11-16 23:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20221116_2357'),
        ('transactions', '0006_auto_20221102_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='acountlesstransaction',
            name='commune',
            field=models.CharField(default='Comuna', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acountlesstransaction',
            name='region',
            field=models.CharField(default='Region', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipping_addresses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='user_profiles.usershippingaddress'),
        ),
        migrations.AlterField(
            model_name='acountlesstransaction',
            name='address',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='acountlesstransaction',
            name='phone_number',
            field=models.CharField(default='+56900000', max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^\\+?1?\\d{8,15}$')]),
            preserve_default=False,
        ),
    ]
