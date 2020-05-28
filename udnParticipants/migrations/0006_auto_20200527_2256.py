# Generated by Django 3.0.6 on 2020-05-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udnParticipants', '0005_auto_20200527_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='reviewItem',
            field=models.CharField(choices=[('Not Reviewed', 'NR'), ('Reviewed - Accepted', 'RA'), ('Not Accepted', 'NA')], default='Not Reviewed', max_length=20),
        ),
    ]
