from django.db import models
from django.utils import timezone


class Movie(models.Model):
    name=models.CharField(max_length=150)
    rate_price=models.DecimalField(max_digits=6,decimal_places=2)
    time=models.DateTimeField()

    def __str__(self):
        return str(self.time)


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.name+','+self.phone


class Ticket(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='users')
    time = models.ForeignKey(Movie,models.CASCADE,related_name='times')
    no_of_tickets = models.PositiveIntegerField()
    booking_time = models.DateTimeField(default = timezone.now)
