from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Player

@login_required
def played(request):
    murders = sorted(set(i.instance.murder for i in
            Player.objects.filter(user__pk__exact=request.user.pk)),
            key=lambda x: x.name)
    return render_to_response('homepage.html', { 'murders': murders },
            context_instance=RequestContext(request))
