# Generated by Django 5.0 on 2023-12-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
