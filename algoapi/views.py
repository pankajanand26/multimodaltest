from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
import algoapi.dijkstra as dj
import json

# Create your views here.

# def home(request):
#     return render(request, 'algoapi/home.html', {})

def home(request):
    G = {'s': {'u': 9, 'x': 5},
         'u': {'v': 1, 'x': 2},
         'v': {'y': 4},
         'x': {'u': 3, 'v': 9, 'y': 2},
         'y': {'s': 7, 'v': 6}}

    (D,P)=dj.Dijkstra(G, 's')
    distances=json.dumps(D)
    prevvert=json.dumps(P)
    print(dj.shortestPath(G, 's', 'v'))

    return HttpResponse("Dijkstra: \nDistances: "+distances+"\nPrevious Vertex: "+prevvert+" Shortest Path is "+' '.join(dj.shortestPath(G, 's', 'v')))
