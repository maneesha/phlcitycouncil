# Generated by Django 4.0.6 on 2022-10-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0003_person_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.CharField(blank=True, choices=[('a', 'Asian'), ('b', 'Black/African American'), ('h', 'Hispanic/Latino'), ('w', 'White'), ('o', 'Other')], max_length=1, null=True),
        ),
    ]
