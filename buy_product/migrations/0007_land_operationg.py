# Generated by Django 3.2.16 on 2023-05-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_product', '0006_land'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='operationg',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=30, null=True),
        ),
    ]
