from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.html import escape as es
from django.http import HttpResponse
import algoapi.dijkstra as dj
import json

# Create your views here.

def home(request):
    return render(request, 'algoapi/home.html', {})

def shortroute(request):
    origin=request.GET.get('origin','')
    destination=request.GET.get('dest','')

    route_details={}

    G = {'s': {'u': 9, 'x': 5},
         'u': {'v': 1, 'x': 2},
         'v': {'y': 4},
         'x': {'u': 3, 'v': 9, 'y': 2},
         'y': {'s': 7, 'v': 6}}

    mode = {'s': {'u': 'bus', 'x': 'train'},
         'u': {'v': 'walk', 'x': 'bus'},
         'v': {'y': 'cab'},
         'x': {'u': 'bus', 'v': 'cab', 'y': 'train'},
         'y': {'s': 'cab', 'v': 'bus'}}


    (D,P)=dj.Dijkstra(G, origin)
    distances=json.dumps(D)
    prevvert=json.dumps(P)
    path=dj.shortestPath(G, origin, destination)
    path_mode=[]
    for i in range(0,len(path)-1):
        path_mode.append(mode[path[i]][path[i+1]])
        # print(path[i + 1])
        # print(mode[path[i]][path[i + 1]])
    # print(D)
    # print(dj.shortestPath(G, origin, destination))
    # print(dj.shortestPath(G, origin, destination))
    route_details['path']=' '.join(path)
    route_details['weight']=D[destination]
    route_details['mode']=' '.join(path_mode)
    route_json=json.dumps(route_details)
    return HttpResponse(route_json)
    # return HttpResponse("Dijkstra: \nDistances: "+distances+"\nPrevious Vertex: "+prevvert+" Shortest Path is "+' '.join(dj.shortestPath(G, origin, destination))+"\n origin: "+origin+" dest: "+destination )
