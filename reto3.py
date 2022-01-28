"""
Autor: Jorge Leonardo Cuellar Dussan

C1 - Semana 4 - Reto 3

El programa de Ingeniería ambiental de la Universidad El Bosque en una de sus salidas de campo, ha registrado un par de temperaturas diarias
(máxima, mínima) para todos los días que permanecieron en campo. Dadas las condiciones del terreno donde se encontraban, no era posible tener 
temperaturas menores de 5 grados ni mayores de 35 grados, que se consideraron errores, pero igual se registraron para su estudio posterior. 
La pareja de temperaturas (0,0) indicará que se han terminado los datos de la salida de campo. El director del programa le ha solicitado a 
usted como programador, que le desarrolle un programa en lenguaje Python que le permita:

• Leer desde el teclado todos los datos registrados en la salida de campo.
• Mostrar en consola el número total de días que duró la salida de campo.
• Mostrar en consola cuantos días en total se tuvieron temperaturas con error, de los cuales se debe informar cuántos fueron por temperaturas
  menores de 5 grados, cuántos fueron por temperaturas mayores de 35 grados y cuántos por ambos errores.
• Mostrar en consola la temperatura media mínima y máxima, sin tener en cuenta los días en que se reportaron errores.
• Mostrar en consola el porcentaje de días que se reportaron errores respecto del total de días reportados.
"""

#Declaro todas las variables y las inicializo
temperatura_minima = temperatura_maxima = suma_temperatura_minima = suma_temperatura_maxima = media_minima = media_maxima =  0.0
mayor_temperatura_error = menor_temperatura_error = 0.0
porcentaje_error = porcentaje_sin_error = mayor_temperatura = menor_temperatura =  0.0

dias = error_mayor = error_menor = doble_error = dias_error = dias_sin_error = 0

#se crea el ciclo para ingresar indeterminados datos, él usuario sera el que le pondra fin al ciclo ingresando 0 y 0 en las temperaturas.
while True:

    #Ingresar por consola las temperaturas
    temperatura_maxima = float(input("Por favor ingrese la temperatura maxima: "))
    #para validar correctamente las temperaturas.
    while True:
        temperatura_minima = float(input("Por favor ingrese la temperatura minima: "))
        if temperatura_minima <= temperatura_maxima:
            break
        else:
            print("\tPor favor ingrese una temperatura que sea menor a la temperatura maxima.")
            print(" ")
#--------------------------------------------------------------------------------------------------------------------------------
    # para salir del registro de temperaturas    
    if temperatura_maxima == 0 and temperatura_minima == 0:
        break
#----------------------------------------------------------------------------------------------------------------------------------- 
    #Contador para saber los dias que permanecieron en campo.
    dias += 1
#--------------------------------------------------------------------------------------------------------------------------------
    #Para revisar las temperaturas tomadas y saber si hay error en la dato o no y realizar registros de variables 
    if temperatura_minima >= 5 and temperatura_maxima <= 35: # Los datos están bien
        dias_sin_error += 1 #contador de dias con temperaturas en el rango establecido
        suma_temperatura_minima += temperatura_minima #Acumulador para ir sumando las temperaturas minimas que esten en el rango establecido
        suma_temperatura_maxima += temperatura_maxima #Acumulador para ir sumando las temperaturas maximas que esten en el rango establecido
        if dias_sin_error == 1: #para la primer temperatura correcta equivaldria a la mayor
            mayor_temperatura = temperatura_maxima
        elif temperatura_maxima > mayor_temperatura:
            mayor_temperatura = temperatura_maxima          
        if dias_sin_error == 1: #para la primer temperatura correcta equivaldria a la menor
            menor_temperatura = temperatura_minima
        elif temperatura_minima < menor_temperatura:
            menor_temperatura = temperatura_minima
        print(" ")
        print("\t==================================================")
        print("\t Temperaturas ingresadas en el rango establecido.")
        print("\t==================================================")
        print("\t Dia de campo ",dias)
        print("\t Temperatura Mínima: ", temperatura_minima,"°")
        print("\t Temperatura Máxima: ", temperatura_maxima,"°")
        print("\t==================================================")
        print(" ")
       
    elif temperatura_minima < 5 and temperatura_maxima  > 35: # Error de ambas temperaturas
        doble_error += 1 #contador de dias con temperaturas fuera del rango establecido
        #Para sacar la temperatura mas alta y baja que esten fuera del rango permitido.
        if dias_sin_error == 1: 
            mayor_temperatura_error = temperatura_maxima
        elif temperatura_maxima > mayor_temperatura_error:
            mayor_temperatura_error = temperatura_maxima 
        if doble_error == 1: 
            menor_temperatura_error = temperatura_minima
        elif temperatura_minima < menor_temperatura_error:
            menor_temperatura_error = temperatura_minima
        print(" ")
        print("\t==============================================")
        print("\t         Error de Ambas Temperaturas")
        print("\t        Temperatura menor a 5 grados")
        print("\t        Temperatura mayor a 35 grados")
        print("\t==============================================")
        print("\t Dia de campo ",dias)
        print("\t Temperatura Mínima fuera del rango: ", temperatura_minima,"°")
        print("\t Temperatura Máxima fuera del rango: ", temperatura_maxima,"°")
        print("\t==============================================")
        print(" ")
     
    elif temperatura_minima < 5 or temperatura_maxima  < 5: # Error de temperatura menor a 5 grados
        error_menor += 1  #contador de dias con temperaturas menores a 5°
        #Para sacar la temperatura mas baja que esten fuera del rango permitido e irla comparando.
        if error_menor == 1: 
            menor_temperatura_error = temperatura_minima
        elif temperatura_minima < menor_temperatura_error:
            menor_temperatura_error = temperatura_minima
        print()
        print("\t===============================================")
        print("\t  Error por temperatura menor a 5 grados")
        print("\t===============================================")
        print("\t Dia de campo ",dias)
        print("\t Temperatura Mínima fuera del rango: ", temperatura_minima,"°")
        print("\t Temperatura Máxima                : ", temperatura_maxima,"°")
        print("\t===============================================")
        print()

    elif temperatura_minima > 35 or temperatura_maxima > 35: # Error de temperatura mayor a 35 grados
        error_mayor += 1 #contador de dias con temperaturas mayores a 35°
        #Para sacar la temperatura mas alta que esten fuera del rango permitido e irla comparando.
        if dias_sin_error == 1: 
            mayor_temperatura_error = temperatura_maxima
        elif temperatura_maxima > mayor_temperatura_error:
            mayor_temperatura_error = temperatura_maxima 
        print(" ")
        print("\t==============================================")
        print("\t  Error por temperatura mayor a 35 grados")
        print("\t==============================================")
        print("\t Dia de campo ",dias)
        print("\t Temperatura Mínima                : ", temperatura_minima,"°")
        print("\t Temperatura Máxima fuera del rango: ", temperatura_maxima,"°")
        print("\t==============================================")
        print(" ")       

#-----------------------------------------------------------------------------------------------------------------------------------
#salgo del ciclo while
#para saber los dias que se registraron errores en la temperatura
dias_error = error_mayor + error_menor + doble_error

# Se calcula la media de la temperatura minima y maxima sin tener encuentra los errores.
if dias_sin_error != 0: #para evitar la divicion por cero
    media_maxima = suma_temperatura_maxima / dias_sin_error
    media_minima = suma_temperatura_minima / dias_sin_error

# Se calcula el porcentaje de días que se reportaron errores respecto del total de días reportados.
if dias != 0: #para evitar la divicion por cero
    porcentaje_error = (dias_error / dias)*100
    porcentaje_sin_error = (dias_sin_error / dias)*100

print("\t=====================================================================")
print("\t                Datos de las temperaturas tomadas")
print("\t=====================================================================")
print("\t Total de dias en campo                                  : ", dias) 
print("\t Total de dias con temperaturas correctas                : ", dias_sin_error)
print("\t=====================================================================")
print("\t Cantidad de dias con temperaturas erroneas              : ", dias_error)
print("\t Cantidad de errores por temperatura menores a 5 grados  : ", error_menor)
print("\t Cantidad de errores por temperatura mayores a 35 grados : ", error_mayor)
print("\t Cantidad de errores por ambas temperaturas              : ", doble_error) 
print("\t=====================================================================")
print("\t Temperatura maxima registrada menor o igual a 35 grados : ", mayor_temperatura,"°")
print("\t Temperatura maxima registada mayor a 35 grados          : ", mayor_temperatura_error,"°")
print("\t Temperatura minima registrada mayor o igual a 5 grados  : ", menor_temperatura,"°")
print("\t Temperatura minima registrada menor a 5 grados          : ", menor_temperatura_error,"°") 
print("\t=====================================================================")
print("\t Temperatura media mínima                                : ", round(media_minima, 3),"°")
print("\t Temperatura media maxima                                : ", round(media_maxima, 3),"°") 
print("\t=====================================================================")
print("\t Porcentaje de dias con temperaturas correctas           : ", round(porcentaje_sin_error, 3),"%") 
print("\t Porcentaje de dias con temperaturas erroneas            : ", round(porcentaje_error, 3),"%") 
print("\t=====================================================================")
print(" ")
input("Presione Enter para continuar.....")
