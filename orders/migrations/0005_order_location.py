# Generated by Django 2.1 on 2018-10-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181029_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]