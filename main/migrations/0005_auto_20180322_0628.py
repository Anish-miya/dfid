# Generated by Django 2.0.3 on 2018-03-22 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180322_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author',
            new_name='capital',
        ),
    ]
