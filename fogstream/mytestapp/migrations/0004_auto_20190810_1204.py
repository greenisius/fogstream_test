# Generated by Django 2.2.4 on 2019-08-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0003_auto_20190810_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]