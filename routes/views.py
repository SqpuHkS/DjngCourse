from django.contrib import messages
from django.shortcuts import render

from routes.forms import RouteForm

def home(request):
    form = RouteForm
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        a = 1
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'We have no data for searching')
        return render(request, 'routes/home.html', {'form': form})