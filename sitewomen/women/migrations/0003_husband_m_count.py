# Generated by Django 4.2.1 on 2024-09-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_remove_husband_m_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
