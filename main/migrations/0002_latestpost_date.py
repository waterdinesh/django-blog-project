# Generated by Django 4.2.2 on 2023-06-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestpost',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
