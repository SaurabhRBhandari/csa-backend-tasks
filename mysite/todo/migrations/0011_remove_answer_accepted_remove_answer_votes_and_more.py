# Generated by Django 4.0 on 2022-02-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_answer_answer_dislikes_answer_answer_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answered',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='views',
        ),
    ]
