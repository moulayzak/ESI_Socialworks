# Generated by Django 4.2 on 2023-05-12 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0033_move_fund'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chapter',
            new_name='Division',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='chapter',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='socialwork',
            old_name='chapter',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='chapter',
            new_name='division',
        ),
    ]