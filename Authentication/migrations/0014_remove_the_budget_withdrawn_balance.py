# Generated by Django 4.2 on 2023-05-08 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0013_socialwork_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='the_budget',
            name='withdrawn_balance',
        ),
    ]