# Generated by Django 4.0 on 2022-01-29 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0009_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_dislikes',
            field=models.ManyToManyField(blank=True, default=None, related_name='answer_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='answer_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]