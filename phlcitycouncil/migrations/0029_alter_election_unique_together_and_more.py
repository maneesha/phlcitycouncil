# Generated by Django 4.0.6 on 2022-11-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0028_alter_candidate_candidate_party'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='election',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='election',
            name='election_party',
            field=models.CharField(blank=True, choices=[('d', 'Democrat'), ('r', 'Republican'), ('i', 'Independent'), ('l', 'Libertarian'), ('wf', 'Working Families Party'), ('p', 'Progressive')], default='', max_length=3, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='election',
            unique_together={('election_date', 'election_type', 'election_seat', 'election_party')},
        ),
    ]
