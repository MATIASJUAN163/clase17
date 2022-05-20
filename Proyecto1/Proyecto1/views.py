from re import template
from django.http import HttpResponse
from django.template import Template, Context

def saludar(request) : 
    return HttpResponse("<h1>Hola, mi primer mensaje desde Django</h1>")

def mayor_edad( resquest , edad ) :
    if edad >= 18 :
        return HttpResponse("<h1 style='color:red'>Usted es mayor</h1>")

    else:
        return HttpResponse("<h1 style='color:blue'>Usted es menor</h1>")

def probando_template(resquest) : 

    mi_html = open("C:/Users/MATIAS/Desktop/DJango/Clase17/Proyecto1/Proyecto1/Plantillas/template.html")
    
    plantilla = Template( mi_html.read() )

    mi_html.close()

    mi_contexto = Context({"nombre":"MATI" , "notas":[10 , 5 , 9 ] })

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

    