from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Player
from catalog.models import Murder

@login_required
def my_played(request):
    return played(request, request.user.pk)

def played(request, user_id):

    player = User.objects.get(pk__exact=user_id)

    # Get the played murders.
    roles = Player.objects.filter(user__pk__exact=user_id)
    done = sorted(set(role.instance.murder for role in roles),
            key=lambda x: x.name)

    # Get the others.
    others = [murder for murder in Murder.objects.all() if murder not in done]

    return render_to_response('played.html',
            { 'player': player, 'played': done, 'others': others,
                'roles': roles },
            context_instance=RequestContext(request))
