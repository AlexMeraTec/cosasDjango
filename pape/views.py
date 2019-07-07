"""pape views."""
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
	now = datetime.now().strftime('%b %d del %Y %H:%M horas')
	return HttpResponse('Olla, Mundo! la fecha en el servidor es : {now}'.format(now=str(now)))

def odenados(request):

    """PRIMERO RECUPERARMOS LA VARIABLE"""
    numeros = request.GET['numeros']
    """LUEGO LE QUITAMOS LAS COMAS"""
    escritos = numeros.split(',')
    """AHORA LA ORDENAMOS CON sorted"""
    ordenados = sorted([int(string) for string in escritos])
    """LUEGO CONVERIMOS LA RESPUESTA AL FORMATO JSON"""
    respuesta = JsonResponse([ordenados], safe=False)
    """FINALMENTE ENVIAMOS LA RESPUESTA"""
    return respuesta
