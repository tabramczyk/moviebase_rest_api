# Generated by Django 2.2.3 on 2019-07-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='rated',
            field=models.CharField(default='', max_length=10),
        ),
    ]
