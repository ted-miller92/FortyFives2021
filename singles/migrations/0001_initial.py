# Generated by Django 3.1.7 on 2021-06-15 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'venues',
                'db_table': 'venue',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]
