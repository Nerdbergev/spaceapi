# Generated by Django 2.2.6 on 2020-10-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191106_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='type',
            field=models.CharField(choices=[('temperature', 'temperature'), ('humidity', 'humidity'), ('barometer', 'barometer'), ('beta_gamma', 'beta_gamma'), ('total_member_count', 'total_member_count'), ('carbondioxide', 'carbondioxide')], max_length=255, null=True),
        ),
    ]
