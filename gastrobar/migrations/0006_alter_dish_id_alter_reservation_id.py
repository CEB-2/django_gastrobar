# Generated by Django 4.0.3 on 2022-03-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastrobar', '0005_merge_0004_alter_dish_photo_0004_merge_20220329_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
