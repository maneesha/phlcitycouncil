# Generated by Django 4.0.6 on 2022-10-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phlcitycouncil', '0002_person_race_alter_seat_seat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='middle_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]