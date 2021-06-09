from django.db import models


def athlete_path(instance, filename):
    return "athlete/" + str(instance.id) + "/photo/" + filename


def flag_path(instance, filename):
    return "country/" + str(instance.id) + "/flag/" + filename


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Official name")

    abbreviation = models.CharField(max_length=3, verbose_name="Official abbreviation")

    flag = models.ImageField(upload_to=flag_path, verbose_name="Flag")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, abb: {str(self.abbreviation)}, flag: {str(self.flag)}"


class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Official name of the discipline")

    GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )

    gender = models.CharField(max_length=5, choices=GENDER, blank=True, default='man',
                              help_text='Select a gender')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Athlete(models.Model):
    name = models.CharField(max_length=20, help_text='John', verbose_name="First name")

    surname = models.CharField(max_length=20, help_text='Smith', verbose_name="Last name")

    birth_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                                  verbose_name="Birth date")

    photo = models.ImageField(upload_to=athlete_path, null=True, verbose_name="Photo")

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    discipline = models.ManyToManyField(Discipline, help_text='Select a discipline the athlete is doing')

    GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )

    gender = models.CharField(max_length=5, choices=GENDER, blank=True, default='man',
                              help_text='Select a gender')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=100, verbose_name="Official name")

    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    athlete = models.ManyToManyField(Athlete, help_text='Select athletes participating on this race')

    discipline = models.ManyToManyField(Discipline, help_text='Select a discipline the athlete is doing')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name



