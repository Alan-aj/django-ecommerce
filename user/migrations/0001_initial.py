# Generated by Django 4.0.2 on 2022-03-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('signid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
