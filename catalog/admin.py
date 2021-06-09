from django.contrib import admin
from .models import Country, Discipline, Athlete, Race

# admin.site.register(Country)
# admin.site.register(Discipline)
# admin.site.register(Athlete)
# admin.site.register(Race)


# Define the admin class
@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "birth_date", "gender")


# Register the admin class with the associated model
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("name", "date")


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("name", "gender")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")

