# Generated by Django 3.0.5 on 2020-07-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200722_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='b0b4b818fb4845a3872251cda78dd006', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default='2f852db264764e2abb6d3f0782ecec39', max_length=200, primary_key=True, serialize=False),
        ),
    ]
