# Generated by Django 4.2 on 2024-05-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatllm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
