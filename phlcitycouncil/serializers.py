from rest_framework import serializers
from .models import Election, Candidate, Person, Seat

# What is a seralizer? 
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types
# https://www.django-rest-framework.org/api-guide/serializers/
# These are imported in the API views in views.py



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


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name = "person_detail_api", format="html")

    class Meta:
        model = Person
        fields = ('id', "first_name", "middle_name",  "last_name", "birth", "death", "race", "gender", "notes", "url")

class CandidateSerializer(serializers.ModelSerializer):

    # election = ElectionSerializer(many = True, read_only = True)
    person = PersonSerializer(many = True, read_only = True)

    class Meta:
        model = Candidate
        depth = 1
        fields = ('candidate_person', 'candidate_election', 'candidate_results', 'candidate_votes_received', 'person')