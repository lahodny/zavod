from django.contrib import admin
from .models import Country, Discipline, Athlete, Race

admin.site.register(Country)
admin.site.register(Discipline)
admin.site.register(Athlete)
admin.site.register(Race)
