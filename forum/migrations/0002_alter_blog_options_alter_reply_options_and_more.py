# Generated by Django 5.0.1 on 2024-02-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['created_at', 'upvote']},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Replies'},
        ),
        migrations.RemoveField(
            model_name='reply',
            name='upvote',
        ),
    ]