# Generated by Django 4.2 on 2023-05-12 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0031_rename_current_balance_the_budget_remaining_budget_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='the_budget',
            name='added_balance',
        ),
    ]