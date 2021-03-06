# Generated by Django 4.0.5 on 2022-06-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('user_name', models.CharField(max_length=45, unique=True)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('mobile_number', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
