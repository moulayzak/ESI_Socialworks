# Generated by Django 4.2 on 2023-05-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0026_rename_phone_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]