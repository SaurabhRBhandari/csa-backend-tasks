# Generated by Django 4.0 on 2022-01-28 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
