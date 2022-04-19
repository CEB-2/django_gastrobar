# Generated by Django 4.0 on 2022-04-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(default=None, max_length=50)),
                ('puesto', models.CharField(default=None, max_length=20)),
                ('description', models.TextField(default=None)),
                ('mail', models.EmailField(default=None, max_length=50)),
            ],
        ),
    ]