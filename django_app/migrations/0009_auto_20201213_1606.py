# Generated by Django 3.1.4 on 2020-12-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0008_auto_20201213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
