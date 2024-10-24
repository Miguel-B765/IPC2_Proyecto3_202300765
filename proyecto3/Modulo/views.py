from django.shortcuts import render
from django.http import HttpResponse

def saludo(response): 
    return HttpResponse("<h1> Saludo </h1>")

def despédida(reponse): 
    return HttpResponse("<h2> Despedida </h2>")
# Create your views here.
