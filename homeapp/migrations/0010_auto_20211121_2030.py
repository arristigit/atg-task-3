# Generated by Django 3.2.5 on 2021-11-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_auto_20210727_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]