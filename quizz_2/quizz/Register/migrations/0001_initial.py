# Generated by Django 2.1 on 2018-10-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('mobnum', models.IntegerField()),
            ],
        ),
    ]
