# Generated by Django 3.0.3 on 2020-02-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
