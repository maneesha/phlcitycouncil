# Generated by Django 4.0.6 on 2022-10-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0008_remove_candidate_candidate_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
