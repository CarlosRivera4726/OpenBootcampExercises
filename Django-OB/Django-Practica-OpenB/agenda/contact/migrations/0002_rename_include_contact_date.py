# Generated by Django 4.1.5 on 2023-01-22 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='include',
            new_name='date',
        ),
    ]