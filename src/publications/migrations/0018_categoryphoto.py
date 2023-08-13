# Generated by Django 3.2.3 on 2022-11-27 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0017_publication_is_accepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_uri', models.TextField()),
                ('image_hash', models.CharField(max_length=256, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='publications.category')),
            ],
        ),
    ]
