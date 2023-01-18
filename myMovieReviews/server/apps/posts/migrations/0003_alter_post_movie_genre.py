# Generated by Django 4.1.5 on 2023-01-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_movie_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='movie_genre',
            field=models.CharField(choices=[('RO', 'Romance'), ('CO', 'Comedy'), ('RC', 'RomCom'), ('AN', 'Animation'), ('HO', 'Horror'), ('DR', 'Drama'), ('AC', 'Action'), ('SF', 'Science Fiction'), ('TJ', 'Tear Jerker'), ('FA', 'Fantasy'), ('CM', 'Classic Movie'), ('DM', 'Disaster Movie'), ('AM', 'Art Movie'), ('DO', 'Documentary'), ('MD', 'Mock Documentary'), ('BL', 'Blockbuster'), ('WH', 'Whodunnit')], default='AC', max_length=2),
        ),
    ]