# Generated by Django 4.0.6 on 2022-08-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artiсles',
            new_name='Articles',
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
    ]
