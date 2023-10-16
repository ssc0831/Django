# Generated by Django 4.2.6 on 2023-10-16 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('hit', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('filename', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('filesize', models.IntegerField(default=0)),
                ('down', models.ImageField(default=0, upload_to='')),
            ],
        ),
    ]