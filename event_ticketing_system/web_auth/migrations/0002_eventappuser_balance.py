# Generated by Django 4.2.7 on 2024-02-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventappuser',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]