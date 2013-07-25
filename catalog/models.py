from django.db import models

class Murder(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=128)
    date = models.SmallIntegerField()
    rating = models.FloatField()
    min_players = models.SmallIntegerField()
    max_players = models.SmallIntegerField()
    organizers = models.SmallIntegerField()
    action_points = models.BooleanField()
    link = models.URLField(null=True)
    synopsis = models.TextField()

class Instance(models.Model):
    murder = models.ForeignKey(Murder)
    date = models.DateTimeField()
