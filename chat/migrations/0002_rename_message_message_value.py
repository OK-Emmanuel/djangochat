# Generated by Django 3.2.16 on 2023-03-07 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='value',
        ),
    ]