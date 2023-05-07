# Generated by Django 3.2.16 on 2023-04-29 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('num_bath', models.IntegerField()),
                ('num_bed', models.IntegerField()),
                ('title_app', models.CharField(max_length=100)),
                ('dates_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
