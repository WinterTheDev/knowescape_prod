# Generated by Django 5.0.7 on 2024-11-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowescape', '0002_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='company_profiles',
        ),
        migrations.AddField(
            model_name='companies',
            name='company_profile',
            field=models.FileField(blank=True, null=True, upload_to='Company_profile/'),
        ),
    ]
