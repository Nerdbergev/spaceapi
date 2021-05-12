from django.db import models

# Create your models here.


class SensorData(models.Model):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    BAROMETER = "barometer"
    BETA_GAMMA = "beta_gamma"
    MEMBER_COUNT = "total_member_count"
    CO2 = "carbondioxide"
    MAXPERSONS = "max_persons_in_space"

    nameChoice = [
        (TEMPERATURE, 'temperature'),
        (HUMIDITY, 'humidity'),
        (BAROMETER, 'barometer'),
        (BETA_GAMMA, 'beta_gamma'),
        (MEMBER_COUNT, 'total_member_count'),
        (CO2, 'carbondioxide'),
        (MAXPERSONS, 'max_persons_in_space'),
    ]

    type = models.CharField(max_length=255, null=True, choices=nameChoice)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=50, null=True)
    value = models.FloatField()
    unit = models.CharField(max_length=10)
    description = models.CharField(max_length=255, null=True)
    updated = models.DateTimeField(auto_now=True)



