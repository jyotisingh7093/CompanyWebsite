# Generated by Django 2.1.7 on 2019-06-10 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_totalpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cpost',
            new_name='top3post',
        ),
    ]
