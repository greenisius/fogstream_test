# Generated by Django 2.2.4 on 2019-08-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='status_code',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='email',
            field=models.EmailField(max_length=40),
        ),
    ]
