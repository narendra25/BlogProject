# Generated by Django 4.2.4 on 2023-08-30 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_contacts_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='ConfirmPassword',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='UserName',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='created_at',
        ),
    ]
