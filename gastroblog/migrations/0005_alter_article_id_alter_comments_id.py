# Generated by Django 4.0.3 on 2022-03-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastroblog', '0004_merge_20220330_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
