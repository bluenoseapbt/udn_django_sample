# Generated by Django 3.0.6 on 2020-05-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udnParticipants', '0003_participant_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='reviewItem',
            field=models.CharField(choices=[('NR', 'Not Reviewed'), ('RA', 'Reviewed - Accepted'), ('NA', 'Not Accepted')], default='Not Reviewed', max_length=20),
        ),
    ]
