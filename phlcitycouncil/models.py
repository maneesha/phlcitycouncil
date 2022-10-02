from django.db import models

# Create your models here.
class Person(models.Model):
    """Model representing a person (not candidate/role)"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    birth = models.DateField()
    death = models.DateField()

    def __str__(self):
        return self.first_name +  " " + self.last_name

class Candiate(models.Model):
    """Model representing a candidate for city council.  May or may not end up holding a seat."""

    pass

class Election(models.Model):
    """Model representing each Election"""

    pass 

class Seat(models.Model):
    """Model representing every possible seat in city council"""

    SEATS = (
        ('1', "1st District",
         '2', "2nd District",
         '3', "3rd District",
         '4', "4th District",
         '5', "5th District",
         '6', "6th District",
         '7', "7th District",
         '8', "8th District",
         '9', "9th District",
         '10', "10th District",
         "AL", "At Large")


    )
    seat_name = models.CharField(max_length = 2, choices = SEATS, blank=False, null=False) 


class Term(models.Model):
    """Model representing every term a Person holds a Seat """

    pass 

