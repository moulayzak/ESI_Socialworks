# Generated by Django 4.2 on 2023-05-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_user_city_user_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('grant', models.IntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='SocialWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Authentication.section')),
            ],
        ),
    ]
