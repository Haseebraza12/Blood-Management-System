# Generated by Django 3.0.5 on 2024-05-18 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_ngo_ngo_name'),
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_ngo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo.Ngo'),
        ),
    ]
