from django.db import models

class Travell(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, null=True, blank=True)
    duration = models.DurationField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    klass = models.CharField(max_length=250)
    klass = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    

class Klass(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=250)
    rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
