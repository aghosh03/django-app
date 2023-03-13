# Generated by Django 4.1.4 on 2023-03-13 00:05

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
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('created_by', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=200)),
                ('details', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'records',
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('receive_emails', models.BooleanField(default=True)),
                ('email_frequency', models.CharField(choices=[('daily', 'Daily'), ('daily', 'Weekly'), ('daily', 'Monthly')], default=('daily', 'Daily'), max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
        ),
    ]