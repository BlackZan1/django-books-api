# Generated by Django 3.0.5 on 2020-07-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='1dd5b410cbf211eaa8e4f07959907aeb', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default='1dd5db20cbf211ea8530f07959907aeb', max_length=200, primary_key=True, serialize=False),
        ),
    ]
