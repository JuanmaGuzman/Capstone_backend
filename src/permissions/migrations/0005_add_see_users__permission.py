# Generated by Django 3.2.3 on 2022-11-17 01:22

from django.db import migrations


def see_all_users(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    userProfile_type = ContentType.objects.get_for_model(
        apps.get_model('user_profiles', 'UserProfile')
    )
    # Create
    see_users_permission = Permission.objects.create(
        codename='obtain_all',
        name='Can see users',
        content_type=userProfile_type
    )

    Group.objects.get(name='Admin').permissions.add(
        see_users_permission,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_add_coupon_permission'),
    ]

    operations = [
        migrations.RunPython(see_all_users),
    ]
