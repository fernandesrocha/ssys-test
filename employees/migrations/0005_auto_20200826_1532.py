# Generated by Django 3.1 on 2020-08-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20200812_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=4, verbose_name="Department's Code"),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=64, verbose_name="Department's Name"),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, verbose_name="Employee's e-mail"),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=64, verbose_name="Employee's Name"),
        ),
    ]