# Generated by Django 5.1.4 on 2025-01-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reflection', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
