from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Person(models.Model):
    """Model representing a person (not candidate/role)"""

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    birth = models.DateField(null = True, blank = True)
    death = models.DateField(null = True, blank = True)

    RACE = (
        ('a', 'Asian'),
        ('b', 'Black/African American'),        
        ('h', 'Hispanic/Latino'),
        ('w', 'White'),
        ('o', 'Other'),

    )

    race = models.CharField(choices = RACE, max_length = 1, null=True, blank=True)

    GENDER = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('o', "Non-binary/other")
    )

    gender = models.CharField(choices = GENDER, max_length=1, null=True, blank=True)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.first_name +  " " + self.last_name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('person-detail', args=[str(self.id)])


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

    class Meta:
        ordering = ['seat_name']

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

    election_seat = models.ForeignKey('Seat', on_delete=models.RESTRICT, null=False, blank=False, related_name = 'seat' )


    class Meta:
        unique_together = ('election_date', 'election_type', 'election_seat')
        ordering = ['election_date', 'election_type', 'election_seat']

    def __str__(self):
        date_string = self.election_date.strftime('%Y')
        election_type_verbose = self.get_election_type_display()
        election_seat_verbose = self.election_seat.get_seat_name_display()

        return election_type_verbose + " Election (" + date_string + "), " + election_seat_verbose


    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('election-detail', args=[str(self.id)])


class Candidate(models.Model):
    """Model representing a candidate for city council.  May or may not end up holding a seat."""
    
    candidate_person = models.ForeignKey("Person", on_delete=models.CASCADE, blank=False, null=False, related_name = "person")
    candidate_election = models.ForeignKey("Election", on_delete=models.CASCADE, blank=False, null=False,)
    # candidate_seat = models.ForeignKey("Seat", on_delete=models.CASCADE, blank=False, null=False)

    PARTIES = (
        ('d', 'Democrat'),
        ('r', 'Republican'),
        ('i', 'Independent'),
        ('l', 'Libertarian'),
        ('wf', 'Working Families Party'),
        ('p', 'Progressive'),
    )

    candidate_party = models.CharField(max_length = 3, choices=PARTIES, blank=True, null=True, default = "")

    RESULTS = (
        ('w', 'Win'),
        ('l', 'Lose'),
    )

    candidate_results = models.CharField(max_length=1, choices=RESULTS, blank=True, null=True)

    candidate_votes_received = models.PositiveIntegerField()

    class Meta:
        ordering = ['candidate_election__election_seat__seat_name']
        unique_together = ('candidate_person', 'candidate_election')


    def __str__(self):
        full_name = self.candidate_person.first_name + " " + self.candidate_person.last_name
        party = self.get_candidate_party_display()
        election_type_verbose = self.candidate_election.get_election_type_display()
        election_seat_verbose = self.candidate_election.election_seat.get_seat_name_display()
        election_date_string = self.candidate_election.election_date.strftime("%Y")
        election_verbose = election_type_verbose + " Election (" + election_date_string + "), " + election_seat_verbose
        return  full_name + "(" + party + "), " + election_verbose


class Term(models.Model):
    """Model representing every term a Person holds a Seat """

    councilmember = models.ForeignKey("Candidate", 
                                      on_delete=models.RESTRICT,
                                      limit_choices_to={'candidate_results': 'w'})
    term_start_date = models.DateField(null = False, blank = False)
    term_end_date = models.DateField(null = False, blank = False)

    left_early = models.BooleanField(null = True, blank = True)
    left_date = models.DateField(null = True, blank = True)

    REASON_FOR_LEAVING = (
        ('a', 'Resigned for another election'),
        ('s', 'Resigned in shame (indicted)'),
        ('r', 'Retired'),
        ('l', 'Lost election'),
        ('t', 'Term ended; re-elected'),
        ('u', 'Unknown'),
    )

    term_end_reason = models.CharField(max_length=1, choices = REASON_FOR_LEAVING, blank=True, null=True ) 

    class Meta:
        ordering = ['term_start_date', 'term_end_date', 'councilmember__candidate_person__last_name']

    def __str__(self):
        member_name = self.councilmember.candidate_person.first_name + " " + self.councilmember.candidate_person.last_name
        term_duration = str(self.term_start_date) + " to " + str(self.term_end_date)
        office = self.councilmember.candidate_election.election_seat.get_seat_name_display()
        return member_name + ", " + term_duration + ", " + office
