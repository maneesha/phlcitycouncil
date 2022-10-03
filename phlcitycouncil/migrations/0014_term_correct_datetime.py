# Generated by Django 4.0.6 on 2022-10-02 22:15

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0013_rename_candidate_resuts_candidate_candidate_results_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='term',
            constraint=models.CheckConstraint(check=models.Q(('term_start_date__lte', django.db.models.expressions.F('term_end_date'))), name='correct_datetime'),
        ),
    ]