# Generated by Django 4.0.6 on 2022-10-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0009_person_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
