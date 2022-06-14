# Generated by Django 4.0.5 on 2022-06-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=45, unique=True),
        ),
    ]