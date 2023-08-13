# Generated by Django 3.2.3 on 2022-10-27 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20221019_0228'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcountlessTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.TextField()),
                ('buyer_lastname', models.TextField()),
                ('rut', models.TextField()),
                ('address', models.TextField()),
                ('requested', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='seller',
        ),
        migrations.AddField(
            model_name='transaction',
            name='requested',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='TransactionPointer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transaction_pointer', to='publications.publication')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transaction_pointer', to='transactions.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='AcountlessTransactionPointer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acountless_transaction_pointer', to='publications.publication')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acountless_transaction_pointer', to='transactions.acountlesstransaction')),
            ],
        ),
    ]
