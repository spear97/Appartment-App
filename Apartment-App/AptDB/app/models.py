from django.db import models

class Apt(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        return "{self.name} {self.address}"

class Amounts(models.Model):
    minimum = models.BigIntegerField()
    maximum = models.BigIntegerField()
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.minimum} {self.maximum}"

class Info(models.Model):
    phone_number = models.CharField(max_length=50)
    url = models.CharField(max_length=2083)
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.phone_number} {self.url}"

class Coords(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)