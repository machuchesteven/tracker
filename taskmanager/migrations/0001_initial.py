# Generated by Django 3.2 on 2021-09-18 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('added_date', models.DateField(auto_now=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='UNTRACKED', max_length=16)),
                ('shareholder', models.CharField(default='Unknown', max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('tool_used', models.CharField(blank=True, max_length=64, null=True)),
                ('category', models.CharField(default='Programming', max_length=16)),
                ('added_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='PENDING', max_length=16)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(blank=True, default='', null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taskmanager.project')),
            ],
        ),
    ]
