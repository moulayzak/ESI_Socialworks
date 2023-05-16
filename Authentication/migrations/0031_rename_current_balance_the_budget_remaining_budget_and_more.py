# Generated by Django 4.2 on 2023-05-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0030_rename_initial_balance_the_budget_allocated_divisions_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='the_budget',
            old_name='current_balance',
            new_name='remaining_budget',
        ),
        migrations.AddField(
            model_name='the_budget',
            name='total_budget',
            field=models.IntegerField(default=0),
        ),
    ]