# Generated by Django 4.0.6 on 2022-10-02 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0007_alter_election_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='candidate_seat',
        ),
    ]
