# Generated by Django 4.0.4 on 2022-08-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_vpstestrecord_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpstestrecord',
            name='user_playlist_selection',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
