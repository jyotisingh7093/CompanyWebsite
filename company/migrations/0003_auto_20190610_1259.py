# Generated by Django 2.1.7 on 2019-06-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190610_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='back_pics/')),
            ],
        ),
        migrations.AlterField(
            model_name='cpost',
            name='backimage',
            field=models.ImageField(upload_to='back_pics/'),
        ),
    ]