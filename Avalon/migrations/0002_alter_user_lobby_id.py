# Generated by Django 5.0.1 on 2024-01-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lobby_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
