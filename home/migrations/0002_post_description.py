# Generated by Django 2.2.6 on 2019-10-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
