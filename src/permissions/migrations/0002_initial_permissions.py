# Generated by Django 3.2.3 on 2022-09-19 21:22

from django.db import migrations


def create_role_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    user_profile_type = ContentType.objects.get_for_model(
        apps.get_model('user_profiles', 'UserProfile')
    )
    # Assign seller
    assign_seller_permission = Permission.objects.create(
        codename='assign_seller',
        name='Can assign seller',
        content_type=user_profile_type
    )
    # Assign admin
    Permission.objects.create(
        codename='assign_admin',
        name='Can assign admin',
        content_type=user_profile_type
    )
    # Assign permission to groups
    Group.objects.get(name='Admin').permissions.add(
        assign_seller_permission
    )


def create_publication_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    publication_type = ContentType.objects.get_for_model(
        apps.get_model('publications', 'Publication')
    )
    # Create
    create_publication_permission = Permission.objects.create(
        codename='can_create',
        name='Can create publication',
        content_type=publication_type
    )
    # Update
    update_publication_permission = Permission.objects.create(
        codename='can_update',
        name='Can update publication',
        content_type=publication_type
    )
    # Remove
    remove_publication_permission = Permission.objects.create(
        codename='can_remove',
        name='Can remove publication',
        content_type=publication_type
    )
    # Allow
    allow_publication_permission = Permission.objects.create(
        codename='can_allow',
        name='Can allow publication',
        content_type=publication_type
    )
    # Assign permissions
    Group.objects.get(name='Seller').permissions.add(
        create_publication_permission,
        update_publication_permission,
        remove_publication_permission
    )
    Group.objects.get(name='Admin').permissions.add(
        create_publication_permission,
        update_publication_permission,
        remove_publication_permission,
        allow_publication_permission
    )


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_permission_groups'),
        ('publications', '__first__'),
        ('user_profiles', '__first__'),
    ]

    operations = [
        migrations.RunPython(create_publication_permission),
        migrations.RunPython(create_role_permissions),
    ]