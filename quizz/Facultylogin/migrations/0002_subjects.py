# Generated by Django 2.1 on 2018-10-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facultylogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=250)),
            ],
        ),
    ]