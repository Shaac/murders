from catalog.models import Murder, Instance
from roles.models import Player
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import datetime

def homepage(request):
    murders = Murder.objects.order_by('name')
    recent = Instance.objects \
            .filter(date__lte=datetime.date.today()) \
            .order_by('-date')[:10]
    next = Instance.objects \
            .filter(date__gte=datetime.date.today()) \
            .order_by('date')[:10]

    return render_to_response('homepage.html', {
        'murders': murders,
        'recent': recent,
        'next': next,
        } ,context_instance=RequestContext(request))

def murder(request, murder_id):
    murder = get_object_or_404(Murder, pk=murder_id)
    instances = Instance.objects.filter(murder__pk=murder_id)
    players = sorted(set(player.user for player in
        Player.objects.filter(role__murder__pk=murder_id)),
        key=lambda x: x.username)

    return render_to_response('murder.html', {
        'murder': murder,
        'instances': instances,
        'players': players,
        }, context_instance=RequestContext(request))
