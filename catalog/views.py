from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Race, Athlete
from django.urls import reverse_lazy
from catalog.forms import RaceModelForm


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
    fields = ['name', 'surname', 'birth_date', 'country']


class RaceCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Race
    fields = ['name', 'date', 'athlete', 'discipline']
    success_url = reverse_lazy('races')
    login_url = '/accounts/login/'
    permission_required = 'catalog.add_race'


class RaceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Race
    form_class = RaceModelForm
    template_name = 'catalog/zavod_update_form.html'
    success_url = reverse_lazy('races')
    login_url = '/accounts/login/'
    permission_required = 'catalog.change_race'


class RaceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Race
    success_url = reverse_lazy('races')
    login_url = '/accounts/login/'
    permission_required = 'catalog.delete_race'


# context_object_name = 'athlete_detail'
# template_name = 'catalog/detail.html'


def error_404(request, exception=None):
    return render(request, 'errors/404.html')


# def error_403(request, exception=None):
#    return render(request,'errors/403.html')
