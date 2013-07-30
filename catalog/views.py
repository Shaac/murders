from catalog.models import Murder
from django.shortcuts import render_to_response, get_object_or_404

def homepage(request):
    murders = Murder.objects.order_by('name')
    return render_to_response('homepage.html', { 'murders': murders })

def murder(request, murder_id):
    murder = get_object_or_404(Murder, pk=murder_id)
    return render_to_response('murder.html', { 'murder': murder })
