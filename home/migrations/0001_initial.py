# Generated by Django 3.1.2 on 2020-10-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('bp', models.CharField(max_length=15)),
                ('pulserate', models.FloatField()),
                ('sugarf', models.FloatField()),
                ('sugarpp', models.FloatField()),
                ('temp', models.FloatField()),
                ('diagnosis', models.TextField()),
                ('medicine', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
