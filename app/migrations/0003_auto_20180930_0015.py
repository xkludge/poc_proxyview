# Generated by Django 2.1.1 on 2018-09-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180930_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
