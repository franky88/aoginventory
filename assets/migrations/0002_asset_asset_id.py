# Generated by Django 4.2.4 on 2023-08-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
