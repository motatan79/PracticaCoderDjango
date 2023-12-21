from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola!")

def saludo2(request):
    return HttpResponse(f"Hola {input('Ingresa tu nombre: ')}!")

def nombre(request, nombre, apellido):
    return HttpResponse(f'{apellido} , {nombre}')

def fecha_hora(request):
    from datetime import datetime
    return HttpResponse(datetime.now())

def tirar_dados(request):
    import random
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse(f'Felicitaciones tiraste el numero {numero}')
    else:
        return HttpResponse(f'Has tirado el dado: {numero}, Vuelve a intentar')