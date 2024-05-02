from django.db import models

# Create your models here.

class TicketModel(models.Model):
    Name=models.CharField(max_length=100)
    Seat_Quantity=models.IntegerField()
    Date=models.DateField()
    Movie_Name = models.CharField(max_length=200)
    def __str__(self):
        return self.Name