# Generated by Django 4.0.6 on 2022-10-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0023_alter_term_left_date_alter_term_left_early'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='term_end_reason',
            field=models.CharField(blank=True, choices=[('a', 'Resigned for another election'), ('s', 'Resigned in shame (indicted)'), ('r', 'Retired'), ('l', 'Lost election'), ('t', 'Term ended; re-elected'), ('u', 'Unknown')], max_length=1, null=True),
        ),
    ]
