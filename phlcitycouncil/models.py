from django.db import models

# Create your models here.
class Person(models.Model):
    """Model representing a person (not candidate/role)"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    birth = models.DateField(null = True, blank = True)
    death = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.first_name +  " " + self.last_name


class Seat(models.Model):
    """Model representing every possible seat in city council"""

    SEATS = (
        ('1', "1st District"),
         ('2', "2nd District"),
         ('3', "3rd District"),
         ('4', "4th District"),
         ('5', "5th District"),
         ('6', "6th District"),
         ('7', "7th District"),
         ('8', "8th District"),
         ('9', "9th District"),
         ('10', "10th District"),
         ("AL", "At Large")


    )
    seat_name = models.CharField(max_length = 2, choices = SEATS, blank=False, null=False, unique=True) 

    def __str__(self):
        return self.get_seat_name_display()



class Election(models.Model):
    """Model representing each Election"""

    election_date = models.DateField(null = False, blank = False)

    ELECTION_TYPES = (
        ('p', 'Primary'),
        ('g', 'General'),
        ('s', 'Special'),
    )

    election_type = models.CharField(max_length=1, choices=ELECTION_TYPES,blank=False, null=False)

    election_seat = models.ForeignKey('Seat', on_delete=models.RESTRICT, null=False, blank=False )

    def __str__(self):
        date_string = self.election_date.strftime('%Y')
        election_type_verbose = self.get_election_type_display()
        election_seat_verbose = self.election_seat.get_seat_name_display()

        return election_type_verbose + " Election (" + date_string + "), " + election_seat_verbose

class Candidate(models.Model):
    """Model representing a candidate for city council.  May or may not end up holding a seat."""
    
    candidate_person = models.ForeignKey("Person", on_delete=models.CASCADE, blank=False, null=False)
    candidate_election = models.ForeignKey("Election", on_delete=models.CASCADE, blank=False, null=False)
    candidate_seat = models.ForeignKey("Seat", on_delete=models.CASCADE, blank=False, null=False)

    RESULTS = (
        ('w', 'Win'),
        ('l', 'Lose'),
    )

    candidate_resuts = models.CharField(max_length=1, choices=RESULTS, blank=True, null=True)

    def __str__(self):
        full_name = self.candidate_person.first_name + " " + self.candidate_person.last_name
        seat_verbose = self.candidate_seat.get_seat_name_display()
        return  full_name + ", " + seat_verbose


class Term(models.Model):
    """Model representing every term a Person holds a Seat """

    councilmember = models.ForeignKey("Candidate", on_delete=models.RESTRICT)
    term_start_date = models.DateField(null = False, blank = False)
    term_end_date = models.DateField(null = False, blank = False)

    left_early = models.BooleanField(null = False, blank = False)
    left_date = models.DateField(null = False, blank = False)

    REASON_FOR_LEAVING = (
        ('a', 'Resigned for another election'),
        ('s', 'Resigned in shame (indicted)'),
        ('r', 'Retired'),
        ('l', 'Lost election'),
        ('t', 'Term ended; re-elected'),
        ('u', 'Unknown'),
    )

    term_end_reason = models.CharField(max_length=1, choices = REASON_FOR_LEAVING, blank=False, null=False ) 

    def __str__(self):
        member_name = self.councilmember.candidate_person.first_name + " " + self.councilmember.candidate_person.last_name
        term_duration = str(self.term_start_date) + " to " + str(self.term_end_date)
        office = self.councilmember.candidate_seat.get_seat_name_display()
        return member_name + ", " + term_duration + ", " + office

