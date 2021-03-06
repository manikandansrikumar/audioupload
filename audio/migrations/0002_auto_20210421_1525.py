# Generated by Django 3.2 on 2021-04-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiobook',
            name='active_flag',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='active_flag',
        ),
        migrations.RemoveField(
            model_name='song',
            name='active_flag',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='song',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
