# Generated by Django 3.0.5 on 2020-07-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200723_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='238ad1f9954d4e2cab96a38079e9c1de', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default='61b0193d6071483594975a8cd7a50d31', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
