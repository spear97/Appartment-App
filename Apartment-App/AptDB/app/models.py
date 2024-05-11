from django.db import models

class Apt(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"Name: {self.name} | Address: {self.address}"

class Amounts(models.Model):
    minimum = models.BigIntegerField()
    maximum = models.BigIntegerField()
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Min: ${self.minimum} | Max: ${self.maximum}"

class Info(models.Model):
    phone_number = models.CharField(max_length=50)
    url = models.CharField(max_length=2083)
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Phone Number:{self.phone_number} | URL:{self.url}"

class Coords(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.long}, {self.lat})"

class Images(models.Model):
    src = models.CharField(max_length=2083)
    apt = models.ForeignKey(Apt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Src: {self.src}"