# Generated by Django 3.2.4 on 2023-10-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('contactno', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=5)),
                ('organtype', models.CharField(max_length=10)),
                ('prev_sur', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('agreement', models.CharField(max_length=100)),
            ],
        ),
    ]
