# Generated by Django 3.1.4 on 2020-12-14 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0012_auto_20201213_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data',
        ),
    ]
