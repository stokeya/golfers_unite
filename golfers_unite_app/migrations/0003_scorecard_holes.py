# Generated by Django 4.2 on 2024-04-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfers_unite_app', '0002_golfer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecard',
            name='holes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
