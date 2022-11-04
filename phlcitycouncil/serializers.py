from rest_framework import serializers
from .models import Election, Candidate, Person, Seat

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('seat_name')

class ElectionSerializer(serializers.ModelSerializer):

    seat = SeatSerializer(many = True, read_only=True)

    class Meta:
        model = Election
        depth = 1
        fields = ('election_date', 'election_type', 'election_seat', 'seat',)


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ("first_name", "middle_name",  "last_name", "birth", "death", "race", "gender", "notes")


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ('candidate_person', 'candidate_election', 'candidate_results', 'candidate_votes_received')