from cities_light.models import City
from django.contrib.auth import get_user_model
from django.db import models

from event_ticketing_system.web_auth.models import EventAppUser

UserModel = get_user_model()


class Event(models.Model):
    MUSIC = 'Music'
    NIGHTLIFE = 'Nightlife'
    PERFORMING_VISUAL_ARTS = 'Performing & Visual Arts'
    HOLIDAYS = 'Holidays'
    HEALTH = 'Health'
    HOBBIES = 'Hobbies'
    BUSINESS = 'Business'
    FOOD_DRINK = 'Food & Drink'

    CATEGORY_CHOICES = [
        (MUSIC, 'Music'),
        (NIGHTLIFE, 'Nightlife'),
        (PERFORMING_VISUAL_ARTS, 'Performing & Visual Arts'),
        (HOLIDAYS, 'Holidays'),
        (HEALTH, 'Health'),
        (HOBBIES, 'Hobbies'),
        (BUSINESS, 'Business'),
        (FOOD_DRINK, 'Food & Drink'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    date_and_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    contact_information = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_events')

    def __str__(self):
        return self.title
