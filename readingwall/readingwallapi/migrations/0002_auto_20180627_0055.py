# Generated by Django 2.0.6 on 2018-06-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingwallapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallposts',
            name='blog_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='wallposts',
            name='wall_context',
            field=models.TextField(blank=True),
        ),
    ]