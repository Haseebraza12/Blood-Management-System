# Generated by Django 3.0.5 on 2024-05-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='ngo_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
