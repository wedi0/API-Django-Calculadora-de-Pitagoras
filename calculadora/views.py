from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.

# Teste para ver se API está online
def hello(request):
    return HttpResponse ("<h1>Hello World<h1/>")


#Calculadora
def calcular(request, a, b, c):

    resultado = 0

    # Checagem para ver se os valores insiridos estão corretos:
    if ((a == 0 and b == 0 and c == 0) or (a != 0 and b != 0 and c != 0)):
        
        
        
        return JsonResponse({'mystring': "---ERROR---Por favor, insira apenas dois valores!---ERROR---"})


    if ((a == 0 and b == 0) or (a == 0 and c == 0) or (c == 0 and b == 0)):
         
        return JsonResponse({'mystring': "---ERROR---Por favor, insira apenas dois valores!---ERROR---"})

    if ((a < 0 or b < 0 or c < 0)):
        
        
        return JsonResponse({'mystring': "---ERROR---Os valores precisam ser maiores de 0!---ERROR---"})


    #Calculando oporeções: 

    if a == 0: #Calculando valor de A(hipotenuza)
        resultado = (b**2 + c**2)**0.5
    
        return JsonResponse({'mystring':"O resultado de A eh {}".format(resultado)})
    elif b == 0: #Calculando o valor do B(cateto)
        if (a > c):
            resultado = (a**2 - c**2)**0.5
            return JsonResponse({'mystring':"O resultado de B eh {}".format(resultado)})
        if (a <= c): #Caso o valor de A seja menor, o tringualo não se trata de um tringualo retangulo.

            return JsonResponse({'mystring':"O valor de A(hipotenuza) deve ser maior que o valor de C." })
    elif c == 0:
        if (a > b):#Calculando o valor do C(cateto)
            resultado = (a**2 - b**2)**0.5
        return JsonResponse({'mystring': ("O resultado de C eh {1}".format(resultado)) })
    else: #Caso o valor de A seja menor, o tringualo não se trata de um tringualo retangulo.
        return JsonResponse({'mystring': "O valor de A(hipotenuza) deve ser maior que o valor de B."})
    
   
