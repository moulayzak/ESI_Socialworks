# Generated by Django 4.2 on 2023-05-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0040_remove_transaction_allocated_withdrawn_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recipe_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
