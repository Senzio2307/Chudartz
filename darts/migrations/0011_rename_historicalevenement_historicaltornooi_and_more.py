# Generated by Django 5.0.6 on 2024-08-29 17:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('darts', '0010_beurtkaart_historicalbeurtkaart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalEvenement',
            new_name='HistoricalTornooi',
        ),
        migrations.RenameModel(
            old_name='Evenement',
            new_name='Tornooi',
        ),
        migrations.AlterModelOptions(
            name='historicaltornooi',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'Geschiedenis', 'verbose_name_plural': 'historical tornoois'},
        ),
    ]