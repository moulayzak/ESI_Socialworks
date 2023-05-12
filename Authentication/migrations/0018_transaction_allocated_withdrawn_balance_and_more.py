# Generated by Django 4.2 on 2023-05-09 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0017_alter_transaction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='allocated_withdrawn_balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.the_budget'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='withdrawn_balance',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
