# Generated by Django 4.2.8 on 2024-01-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
    ]
