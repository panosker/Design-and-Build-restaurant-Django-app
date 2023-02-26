from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory =models.IntegerField()

    def __str__(self) :
        return f"{self.title}:{str(self.price)}"

class Bookings(models.Model):
    name =models.CharField(max_length=255)
    No_of_guests= models.SmallIntegerField(default=6)
    BookingDate= models.DateTimeField()

    def __str__(self) :
        return self.name

