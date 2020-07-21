# Generated by Django 3.0.6 on 2020-07-21 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_virtual_circuit_plugin', '0002_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualcircuit',
            name='vcid',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(4294967295), django.core.validators.MinValueValidator(1)]),
        ),
    ]
