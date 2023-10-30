# Generated by Django 4.2.6 on 2023-10-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp03', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('tmef', models.TextField(null=True)),
                ('wf', models.TextField(null=True)),
                ('tmn', models.IntegerField(default=0)),
                ('tmx', models.IntegerField(default=0)),
            ],
        ),
    ]
