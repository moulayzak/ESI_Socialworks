# Generated by Django 4.2 on 2023-05-12 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0037_rename_move_fund_move_income_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='current_balance',
            new_name='remaining_allocated_amount',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='added_balance',
        ),
    ]
