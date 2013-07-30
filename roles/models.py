from django.db import models
from catalog.models import Murder, Instance
from django.contrib.auth.models import User

class Role(models.Model):
    murder = models.ForeignKey(Murder)
    name = models.CharField(max_length=128)
    organizer = models.BooleanField()
    male = models.BooleanField()
    female = models.BooleanField()
    optional = models.BooleanField()

    def __unicode__(self):
        return self.name

class Player(models.Model):
    role = models.ForeignKey(Role)
    instance = models.ForeignKey(Instance)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.user) + " as " + str(self.role)
