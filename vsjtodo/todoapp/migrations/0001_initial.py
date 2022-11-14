# Generated by Django 4.0.2 on 2022-11-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('dateoftask', models.DateTimeField()),
            ],
        ),
    ]
