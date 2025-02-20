# Generated by Django 3.1.1 on 2021-03-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', models.TextField()),
                ('tag', models.CharField(max_length=50, verbose_name='Tag')),
                ('image', models.ImageField(upload_to='image/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
    ]
