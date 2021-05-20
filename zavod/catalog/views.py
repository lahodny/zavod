from django.shortcuts import render
from django.views import generic

from catalog.models import Race, Athlete


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    num_races = Race.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    races = Race.objects.order_by('-date')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_races': num_races,
        'races': races
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class RaceListView(generic.ListView):
    model = Race


class RaceDetailView(generic.DetailView):
    model = Race


class AthleteListView(generic.ListView):
    model = Athlete


class AthleteDetailView(generic.DetailView):
    model = Athlete

