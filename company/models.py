from django.db import models


class Salary(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.amount}'


class Job(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'


class Country(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    Country_code = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Place(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    zip_code = models.CharField(max_length=5, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.name }'


class Employee(models.Model):
    id_number = models.IntegerField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField()
    address = models.CharField(max_length=50, null=False, blank=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
