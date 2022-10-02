from django.contrib import admin

# Register your models here.

from .models import Person, Seat, Election, Candidate, Term

admin.site.register(Person)
admin.site.register(Seat)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Term)