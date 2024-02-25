# Generated by Django 4.2.10 on 2024-02-23 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Calling')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Family')),
                ('address', models.TextField(verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Quorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quorum_name', models.TextField(verbose_name='Quorum/Class')),
                ('quorum_min_date', models.DateField(verbose_name='Minimum date cutoff')),
                ('quorum_max_date', models.DateField(verbose_name='Maximum date cutoff')),
            ],
        ),
        migrations.CreateModel(
            name='Stake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Stake')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Ward')),
                ('stake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.stake')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthdate', models.DateField(verbose_name='Birthday')),
                ('callings', models.ManyToManyField(to='directories.calling')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='directories.family')),
                ('quorum', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='directories.quorum')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='directories.ward')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('attendees', models.ManyToManyField(to='directories.user')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.user')),
            ],
        ),
    ]