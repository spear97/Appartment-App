# Generated by Django 5.0.4 on 2024-04-19 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('apt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apt')),
            ],
        ),
    ]
