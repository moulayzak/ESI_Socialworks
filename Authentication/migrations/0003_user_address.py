# Generated by Django 4.2 on 2023-05-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]