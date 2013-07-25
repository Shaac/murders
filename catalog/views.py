from catalog.models import Murder
from django.shortcuts import render_to_response

def homepage(request):
    murders = Murder.objects.all()
    return render_to_response('homepage.html', { 'murders': murders })
