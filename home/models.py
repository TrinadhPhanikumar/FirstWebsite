from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bp = models.CharField(max_length=10)
    pulserate = models.FloatField()
    sugarf = models.FloatField()
    sugarpp = models.FloatField()
    temp = models.FloatField()
    diagnosis = models.TextField()
    medicine = models.TextField()
    #image = models.FileField(null=True, default='none')

    reference = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name


class Listimages(models.Model):
    details = models.ForeignKey('List', null=True, on_delete=models.CASCADE)
    image = models.FileField(null=True, default='none')

    def __str__(self):
        return self.details.name
