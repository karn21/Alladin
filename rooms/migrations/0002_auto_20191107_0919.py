# Generated by Django 2.1.5 on 2019-11-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.CharField(default=2, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='plan',
            field=models.CharField(default='deluxe', max_length=50),
            preserve_default=False,
        ),
    ]
