# Generated by Django 4.2.7 on 2024-01-27 15:51

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_and_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Nightlife', 'Nightlife'), ('Performing & Visual Arts', 'Performing & Visual Arts'), ('Holidays', 'Holidays'), ('Health', 'Health'), ('Hobbies', 'Hobbies'), ('Business', 'Business'), ('Food & Drink', 'Food & Drink')], max_length=50)),
                ('contact_information', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
