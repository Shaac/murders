from catalog.models import Murder
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def homepage(request):
    murders = Murder.objects.order_by('name')
    return render_to_response('homepage.html', { 'murders': murders },
            context_instance=RequestContext(request))

def murder(request, murder_id):
    murder = get_object_or_404(Murder, pk=murder_id)
    return render_to_response('murder.html', { 'murder': murder },
            context_instance=RequestContext(request))
