# Generated by Django 4.0.3 on 2022-04-09 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='detetime_created',
            new_name='datetime_created',
        ),
    ]
