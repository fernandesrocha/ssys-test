# Generated by Django 3.1 on 2020-08-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20200808_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]
