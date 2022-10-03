from django.shortcuts import render
from django.views import generic 

from .models import Person, Seat

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