# Generated by Django 5.1.6 on 2025-03-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepagedesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
