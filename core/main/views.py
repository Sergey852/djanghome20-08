from django.shortcuts import render
from .models import Cattleya
from .models import Dendrobium
from .models import Chiloschista
from .models import Vanda

# Create your views here.
def home(request):
    return render(request, 'home.html')
def cattleya(request):
    mylist = Cattleya.objects.all()
    return render(request, 'cattleya.html', {'mylist':mylist})
def dendrobium(request):
    dendr = Dendrobium.objects.all()
    return render(request, 'dendrobium.html', {'dendr':dendr})
def chiloschista(request):
    chil = Chiloschista.objects.all()
    return render(request, 'chiloschista.html', {'chil':chil})
def vanda(request):
    vand = Vanda.objects.all()
    return render(request, 'vanda.html', {'vand':vand})
    
