# Generated by Django 3.2.12 on 2022-05-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
