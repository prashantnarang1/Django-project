# Generated by Django 5.0.1 on 2024-01-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gundepot', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'Assault Rifles'), (2, 'Designated Marksman Rifles'), (3, 'Sniper Rifles'), (4, 'Shotguns'), (5, 'Light Machine Guns'), (6, 'Submachine Guns'), (7, 'Pistols'), (8, 'Crossbows'), (9, 'Melee Weapons'), (10, 'Throwables')]),
        ),
    ]
