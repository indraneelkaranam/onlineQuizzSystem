# Generated by Django 2.1 on 2018-10-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_registerlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerlist',
            name='mobnum',
            field=models.CharField(max_length=250),
        ),
    ]
