# Generated by Django 4.2.13 on 2024-07-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_remove_galleryitems_file_galleryitems_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitems',
            name='url_tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
