# Generated by Django 3.1.7 on 2021-06-16 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FortyFive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistname', models.CharField(max_length=255)),
                ('label', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('sideone', models.TextField(blank=True, null=True)),
                ('sidetwo', models.TextField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'fortyfives',
                'db_table': 'fortyfive',
            },
        ),
        migrations.CreateModel(
            name='RecordStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=255)),
                ('storelocation', models.TextField(blank=True, null=True)),
                ('businesshours', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'recordstores',
                'db_table': 'recordstore',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venuename', models.CharField(max_length=255)),
                ('venuelocation', models.TextField(blank=True, null=True)),
                ('venueinfo', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
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
                ('eventname', models.CharField(max_length=255)),
                ('eventinfo', models.TextField(blank=True, null=True)),
                ('eventdate', models.DateField()),
                ('eventurl', models.URLField(blank=True, null=True)),
                ('venuelocation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='singles.venue')),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]
