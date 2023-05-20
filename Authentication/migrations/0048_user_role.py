# Generated by Django 4.2 on 2023-05-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0047_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('EMPLOYEE ', 'Employee'), ('SOCIAL WORK COMITTEE', 'Social Work Comittee')], default='EMPLOYEE', max_length=20),
        ),
    ]