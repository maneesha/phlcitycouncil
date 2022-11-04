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

