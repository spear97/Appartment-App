# Generated by Django 5.0.4 on 2024-04-18 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_delete_apt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Amounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.BigIntegerField()),
                ('maximum', models.BigIntegerField()),
                ('apt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apt')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=2083)),
                ('apt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apt')),
            ],
        ),
    ]