# Generated by Django 2.2.3 on 2019-07-15 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0008_auto_20190715_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commented_film',
            new_name='movie',
        ),
    ]
