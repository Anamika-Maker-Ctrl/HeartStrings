# Generated by Django 4.2.5 on 2023-10-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar_app', '0002_organ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='organtype',
            field=models.CharField(max_length=100),
        ),
    ]