# Generated by Django 4.0.4 on 2022-05-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='hide_email',
            new_name='mailing_list',
        ),
    ]
