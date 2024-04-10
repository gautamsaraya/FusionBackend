# Generated by Django 3.1.5 on 2024-04-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0019_merge_20240315_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestroom',
            name='room_type',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], default='single', max_length=10),
        ),
        migrations.AddField(
            model_name='guestroombooking',
            name='room_type',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], default='single', max_length=10),
        ),
    ]
