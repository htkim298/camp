# Generated by Django 2.1.15 on 2020-09-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolViewData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camdate', models.CharField(max_length=200)),
                ('cametc', models.CharField(max_length=200)),
                ('asite', models.IntegerField()),
                ('bsite', models.IntegerField()),
                ('csite', models.IntegerField()),
                ('dsite', models.IntegerField()),
                ('esite', models.IntegerField()),
            ],
            options={
                'db_table': 'solcamp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
