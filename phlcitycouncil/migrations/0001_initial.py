# Generated by Django 4.0.6 on 2022-10-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_resuts', models.CharField(blank=True, choices=[('w', 'Win'), ('l', 'Lose')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth', models.DateField(blank=True, null=True)),
                ('death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_name', models.CharField(choices=[('1', '1st District'), ('2', '2nd District'), ('3', '3rd District'), ('4', '4th District'), ('5', '5th District'), ('6', '6th District'), ('7', '7th District'), ('8', '8th District'), ('9', '9th District'), ('10', '10th District'), ('AL', 'At Large')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_start_date', models.DateField()),
                ('term_end_date', models.DateField()),
                ('left_early', models.BooleanField()),
                ('left_date', models.DateField()),
                ('term_end_reason', models.CharField(choices=[('a', 'Resigned for another election'), ('s', 'Resigned in shame (indicted)'), ('r', 'Retired'), ('l', 'Lost election'), ('t', 'Term ended; re-elected'), ('u', 'Unknown')], max_length=1)),
                ('councilmember', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='phlcitycouncil.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_date', models.DateField()),
                ('election_type', models.CharField(choices=[('p', 'Primary'), ('g', 'General'), ('s', 'Special')], max_length=1)),
                ('election_seat', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='phlcitycouncil.seat')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='candidate_election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phlcitycouncil.election'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='candidate_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phlcitycouncil.person'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='candidate_seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phlcitycouncil.seat'),
        ),
    ]