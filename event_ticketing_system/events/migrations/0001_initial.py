# Generated by Django 4.2.7 on 2023-12-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('total_tickets', models.PositiveIntegerField()),
                ('available_tickets', models.PositiveIntegerField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('organizer', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Nightlife', 'Nightlife'), ('Performing & Visual Arts', 'Performing & Visual Arts'), ('Holidays', 'Holidays'), ('Health', 'Health'), ('Hobbies', 'Hobbies'), ('Business', 'Business'), ('Food & Drink', 'Food & Drink')], max_length=50)),
                ('contact_information', models.CharField(max_length=255)),
            ],
        ),
    ]
