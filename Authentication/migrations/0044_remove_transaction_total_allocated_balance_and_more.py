# Generated by Django 4.2 on 2023-05-12 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0043_rename_the_budget_fund_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='total_allocated_balance',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='total_income_balance',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='total_withdrawn_payouts_balance',
        ),
    ]