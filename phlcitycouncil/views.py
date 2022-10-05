from django.shortcuts import render
from django.views import generic 
from django.db.models.functions import ExtractYear


from .models import Person, Seat, Election

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
    model = Election 
