# Generated by Django 2.2 on 2019-12-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_personnage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnage',
            name='publie',
            field=models.BooleanField(default=True),
        ),
    ]