from django.shortcuts import render
from django.views import generic 
from django.db.models.functions import ExtractYear

from rest_framework import generics
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ElectionSerializer, PersonSerializer, CandidateSerializer


from .models import Person, Seat, Election, Term, Candidate

# Create your views here.

def index(request):

    """ View function for home page """

    num_persons = Person.objects.all().count()
    num_seats = Seat.objects.all().count()

    context = {
        'num_persons':num_persons,
        'num_seats':num_seats,
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

    def get_queryset(self):
        # return Election.objects.filter(election_type = 's')
        queryset = {
            'election':Election.objects.all(),
            'special':Election.objects.filter(election_type = 's').values(),
            'primary':Election.objects.filter(election_type = 'p'),
            'general':Election.objects.filter(election_type = 'g'),
            'years': Election.objects.order_by().values('election_date').distinct().annotate(year=ExtractYear('election_date')).values('year'),
            'types':Election.objects.order_by().values('election_type').distinct(),
        }
        return queryset

class ElectionDetailView(generic.DetailView):
    """
    Specifying model = Election is shorthand for saying queryset = Election.objects.get(pk=primary_key). 
    https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/
    """
    model = Election 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cand'] = Election.objects.filter(pk=self.kwargs.get('pk'))
        context['qu'] = Election.objects.all()
        # context['baseball'] = 'phillies'
        # context['cand'] = Candidate.objects.all()
        # context['pers'] = Person.objects.all()
        return context 



class TermView(generic.ListView):
    model = Term 


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