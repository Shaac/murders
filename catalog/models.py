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

    def __unicode__(self):
        return self.name

class Instance(models.Model):
    murder = models.ForeignKey(Murder)
    date = models.DateTimeField()

    def __unicode__(self):
        return str(self.murder) + " " + self.date.strftime("%d/%m/%y")
