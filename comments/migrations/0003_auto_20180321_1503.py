# Generated by Django 2.0.3 on 2018-03-21 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180319_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
    ]