# Generated by Django 3.2.3 on 2022-09-27 23:53

from django.db import migrations


def create_transaction_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    transaction_type = ContentType.objects.get_for_model(
        apps.get_model('transactions', 'Transaction')
    )
    # Create
    create_transaction_permission = Permission.objects.create(
        codename='can_create',
        name='Can create transaction',
        content_type=transaction_type
    )
    # Read
    read_transactions_permission = Permission.objects.create(
        codename='can_read',
        name='Can read transaction',
        content_type=transaction_type
    )
    # Confirm
    confirm_transaction_permission = Permission.objects.create(
        codename='can_confirm',
        name='Can confirm transaction',
        content_type=transaction_type
    )
    Group.objects.get(name='Seller').permissions.add(
        create_transaction_permission
    )
    Group.objects.get(name='Admin').permissions.add(
        read_transactions_permission,
        confirm_transaction_permission
    )


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_initial_permissions'),
        ('transactions', '__first__')
    ]

    operations = [
        migrations.RunPython(create_transaction_permissions)
    ]
