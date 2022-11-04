from rest_framework import serializers
from .models import Election, Candidate, Person 

class ElectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Election

        fields = ('election_date', 'election_type', 'election_seat')

