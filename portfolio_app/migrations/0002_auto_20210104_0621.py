# Generated by Django 3.1.3 on 2021-01-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_site',
            field=models.URLField(blank=True),
        ),
    ]
