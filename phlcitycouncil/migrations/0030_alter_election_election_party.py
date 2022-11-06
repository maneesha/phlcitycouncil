# Generated by Django 4.0.6 on 2022-11-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0029_alter_election_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_party',
            field=models.CharField(choices=[('d', 'Democrat'), ('r', 'Republican'), ('i', 'Independent'), ('l', 'Libertarian'), ('wf', 'Working Families Party'), ('p', 'Progressive')], default='', max_length=3),
        ),
    ]
