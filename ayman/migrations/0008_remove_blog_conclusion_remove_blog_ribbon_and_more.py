# Generated by Django 4.2.1 on 2023-05-29 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ayman', '0007_achievement_introduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='conclusion',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='ribbon',
        ),
        migrations.RemoveField(
            model_name='project',
            name='conclusion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ribbon',
        ),
    ]