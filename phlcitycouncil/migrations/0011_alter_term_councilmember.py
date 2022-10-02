# Generated by Django 4.0.6 on 2022-10-02 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0010_alter_person_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='councilmember',
            field=models.ForeignKey(limit_choices_to={'candidate_results': 'w'}, on_delete=django.db.models.deletion.RESTRICT, to='phlcitycouncil.candidate'),
        ),
    ]
