# Generated by Django 4.0.6 on 2022-10-03 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0020_alter_seat_options_alter_term_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='candidate',
            unique_together={('candidate_person', 'candidate_election')},
        ),
    ]
