# Generated by Django 3.0.5 on 2024-05-19 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('blood', '0005_bloodrequest_request_by_ngo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
    ]
