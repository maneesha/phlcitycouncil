# Generated by Django 4.0.6 on 2022-11-05 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0024_alter_term_term_end_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='election', to='phlcitycouncil.election'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='phlcitycouncil.person'),
        ),
        migrations.AlterField(
            model_name='election',
            name='election_seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seat', to='phlcitycouncil.seat'),
        ),
    ]
