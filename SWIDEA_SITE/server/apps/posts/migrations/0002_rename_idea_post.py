# Generated by Django 4.1.5 on 2023-01-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Idea',
            new_name='Post',
        ),
    ]
