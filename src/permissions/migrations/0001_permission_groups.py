# Generated by Django 3.2.3 on 2022-09-19 21:22

from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name='Seller')
    Group.objects.create(name='Admin')


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('contenttypes', '__latest__')
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
