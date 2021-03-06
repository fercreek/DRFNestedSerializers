from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    contractors = models.ManyToManyField(Contractor)

    def __strt__(self):
        return self.group_name
