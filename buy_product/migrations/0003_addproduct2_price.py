# Generated by Django 3.2.16 on 2023-05-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_product', '0002_addproduct2'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct2',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
