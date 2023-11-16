# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .admin import StateSelection

def index(request):
    return render(request, 'map.html')

def map_view(request):
    return render(request, 'map.html')

@csrf_exempt  # Temporarily disable CSRF for demonstration
def submit_state(request):
    if request.method == 'POST':
        state_id = request.POST.get('stateId')
        state_name = request.POST.get('stateName')
        StateSelection.objects.create(state_id=state_id, state_name=state_name)
        return redirect('map')  # Redirect back to the map