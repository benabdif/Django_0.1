# Generated by Django 3.2.16 on 2023-04-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]