from django import http

def home(request):
    return http.HttpResponse('iniciando con Django para el profesor bababa!')
