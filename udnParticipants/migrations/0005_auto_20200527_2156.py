# Generated by Django 3.0.6 on 2020-05-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udnParticipants', '0004_auto_20200527_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='siblings',
            field=models.BooleanField(default=False, help_text='Click on the checkbox if you have siblings'),
        ),
    ]
