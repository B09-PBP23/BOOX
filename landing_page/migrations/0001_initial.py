# Generated by Django 4.2.6 on 2023-10-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image_url_s', models.URLField(blank=True, null=True)),
                ('image_url_m', models.URLField(blank=True, null=True)),
                ('image_url_l', models.URLField(blank=True, null=True)),
                ('total_ratings', models.FloatField(default=0)),
                ('total_reviews', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]