# Generated by Django 3.0.3 on 2020-06-11 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_mdl',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
    ]
