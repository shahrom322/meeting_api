# Generated by Django 4.0.1 on 2022-01-15 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser_likes_for_users_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='male',
            new_name='sex',
        ),
    ]
