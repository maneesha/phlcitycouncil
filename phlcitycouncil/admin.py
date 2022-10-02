from django.contrib import admin

# Register your models here.

from .models import Person, Seat, Election, Candidate, Term

# admin.site.register(Person)
admin.site.register(Seat)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Term)

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth', 'death')
    fields = ['first_name', 'middle_name', 'last_name', 'gender', 'race', ('birth', 'death')]
    inlines = [CandidateInline]