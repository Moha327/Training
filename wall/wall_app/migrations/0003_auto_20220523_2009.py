# Generated by Django 2.2.4 on 2022-05-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_comment_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.User'),
            preserve_default=False,
        ),
    ]
