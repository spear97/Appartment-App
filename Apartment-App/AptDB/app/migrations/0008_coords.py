# Generated by Django 5.0.4 on 2024-04-19 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_coords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.FloatField()),
                ('lat', models.FloatField()),
                ('apt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apt')),
            ],
        ),
    ]
