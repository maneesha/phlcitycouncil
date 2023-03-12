from django.shortcuts import render
from django.views import generic 
from django.db.models.functions import ExtractYear
from django.http import JsonResponse
from django.core import serializers

from rest_framework import generics
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ElectionSerializer, PersonSerializer, CandidateSerializer

import json

from .models import Person, Seat, Election, Term, Candidate

# Create your views here.

def index(request):

    """ View function for home page """

    num_persons = Person.objects.all().count()
    num_seats = Seat.objects.all().count()
    num_elections = Election.objects.all().count()

    context = {
        'num_persons':num_persons,
        'num_seats':num_seats,
        'num_elections':num_elections
    }

    return render(request, 'index.html', context=context)

class PersonView(generic.ListView):
    model = Person

class PersonDetailView(generic.DetailView):
    model = Person

class ElectionView(generic.ListView):
    model = Election
    template_name = "phlcitycouncil/election_list.html"
    context_object_name = 'election'

    distinct_elections_query = Election.objects.order_by().values_list('election_date__year', 'election_type').distinct()

    election_list = [] 
    # Create list of values for Election list view/template
    for i in distinct_elections_query:
        year = i[0]
        elec_type = i[1]
        elec_type_dict = {'g':'general', 's':'special', 'p': 'primary'}
        election_tag = elec_type_dict[elec_type] + str(year)
        election_text = elec_type_dict[elec_type] + " Election " + str(year)
        election_list.append([election_tag, election_list])


    def get_queryset(self):

        distinct_elections_query = Election.objects.order_by().values_list('election_date__year', 'election_type').distinct()

        election_list = [] 
       
        # Create list of values for Election list view/template
        for i in distinct_elections_query:

            year = i[0]
            elec_type = i[1]
            elec_type_dict = {'g':'general', 's':'special', 'p': 'primary'}
            election_tag = elec_type_dict[elec_type] + str(year)
            election_text =  elec_type_dict[elec_type].capitalize()  + " Election " + str(year)
            election_query = Election.objects.filter(election_date__year = year).filter(election_type = elec_type)
            # year is used to sort the list of dicts; election_tag is used for html ids; election_text is html text headings; query is to run the query
            x = {"election_year":year, "election_tag" : election_tag, "election_text":election_text, "election_query":election_query}
            election_list.append(x)

        election_list = sorted(election_list, key=lambda d: d['election_year'], reverse=True )

        queryset = {
            'election':Election.objects.all(),
            'election_list': election_list,
        }
        return queryset

class ElectionDetailView(generic.DetailView):
    """
    Specifying model = Election is shorthand for saying queryset = Election.objects.get(pk=primary_key). 
    https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/
    """


    # context_object_name = 'election'
    # queryset = Election.objects.all()
    model = Election 

    def get_context_data(self, **kwargs):
        model = Election
        # el = Election.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        # context['data_list'] = Election.objects.all()

        # Hold queryset in a variable to be used later for candidate/vote count lists
        q1 = Election.objects.filter(pk=self.kwargs.get('pk')).values('id', 'election_date', 'candidate__candidate_results', 'candidate__candidate_person__last_name', 'candidate__candidate_votes_received')
        context['data_list'] = Election.objects.filter(pk=self.kwargs.get('pk')).values('id', 'election_date', 'candidate__candidate_results', 'candidate__candidate_person__last_name', 'candidate__candidate_votes_received')
        # context['data_list'] = Election.objects.select_related()
        context['items'] = Election.objects.values_list('election_date')

        # Create list of candidate names 
        candidates_names = []
        for i in q1: 
            print(i['candidate__candidate_person__last_name'])
            candidates_names.append(i['candidate__candidate_person__last_name'])

        # Create list of vote counts
        vote_count = []
        for i in q1:
            print(i['candidate__candidate_votes_received'])
            vote_count.append(i['candidate__candidate_votes_received'])

        # Add candidate names and vote count lists to context data 
        context['candidates'] = candidates_names
        context['vote_count'] = vote_count 

        results = {}

        for i in q1:
            cn = i['candidate__candidate_person__last_name']
            vr = i['candidate__candidate_votes_received']
            results[cn] = vr


        print(results)
        context['results'] = results

        return context 

class TermView(generic.ListView):
    model = Term 

# Serializers are all defined in serilazers.py
# Associated views for the API are defined here
# URLs based on these vies are set up in urls.py

class ElectionListAPI(generics.ListAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class ElectionDetailAPI(generics.RetrieveAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class PersonListAPI(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailAPI(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CandidateListAPI(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetailAPI(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'persons': reverse('person_list_api', request=request,format=format),
        'candidates': reverse('candidate_list_api', request=request, format=format),
        'elections': reverse('election_list_api', request=request, format=format)
    })