"""
Autor: Jorge Leonardo Cuellar Dussan
Fecha: 30/05/2021

El departamento de Talento Humano de la Universidad El Bosque, a raíz de la participación en un proyecto muy especial, requiere poder procesar 
la nómina de docentes contratados por horas. Para tal efecto ha establecido los siguientes lineamientos:

• La nómina será procesada semanalmente, digitando por cada docente las horas trabajadas en la semana y el valor establecido por hora.
• A todos los docentes que trabajen más de 40 horas en la semana, se les reconocerán como horas extras y se pagarán a un valor de 1,5 de la 
  hora normal.
• Al salario bruto obtenido en el punto anterior se le calculará el 9% para los parafiscales.
• Para cada docente se le calcularán provisiones para prima de servicio 8.33%, cesantías 8.33%, intereses de cesantía 1.0% y vacaciones 4.17%.
• A cada uno se le descontará el aporte de 4% para salud y el 4% para pensión.

El director de Talento Humano le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:

• Leer desde el teclado los datos de nombre, horas trabajadas y valor hora, por cada docente del proyecto.
• Mostrar en consola el sueldo bruto.
• Mostrar en consola los descuentos por parafiscales, salud y pensión.
• Mostrar en consola el sueldo neto a pagar.
• Mostrar en consola las provisiones hechas para prima, cesantías, intereses de cesantía y vacaciones.
• Los cálculos de sueldo bruto, descuentos, sueldo neto y provisiones, deberán ser realizados a través de funciones o procedimientos y serán 
  llamados en el programa principal.
"""

# para calcular el sueldo bruto 
def sueldo_bruto(valor_hora, horas_trabajadas):
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40 #para saber cuantas horas extras trabajo, se le resta 40 que son las horas normales de trabajo
        valor_horas_extras = horas_extras * valor_hora * 1.5 #para saber el precio que tienen dichas horas extras
        sueldo_sin_extras = (horas_trabajadas - horas_extras) * valor_hora #para saber el sueldo sin contar las horas extras
        s_bruto = sueldo_sin_extras + valor_horas_extras #para saber el sueldo que obtuvo contando las horas extras
    else:
        horas_extras = valor_horas_extras = 0 #para poder poner solo un return para esta funcion
        sueldo_sin_extras = s_bruto = horas_trabajadas * valor_hora #sueldo sin tener horas extras
    return s_bruto, horas_extras, valor_horas_extras, sueldo_sin_extras

# para calcular todos los descuentos al sueldo bruto: parafiscales 9%; salud y pension 4% c/u.   
def descuentos(s_bruto):
    parafiscales = s_bruto * 0.09
    salud = pension = 0.04 * s_bruto
    suma_descuentos = parafiscales + salud + pension
    return parafiscales, salud, pension, suma_descuentos

#Para calcular cada una de las provisiones para prima de servicio 8.33%, cesantías 8.33%, intereses de cesantía 1.0% y vacaciones 4.17%.
def provisiones (sueldo_sin_extras, valor_horas_extras):
    prima_servicio = cesantias = (0.0833 * sueldo_sin_extras) + (0.0833 * valor_horas_extras)
    intereses_cesantias = (0.01 * sueldo_sin_extras) + (0.01 * valor_horas_extras)
    vacaciones = (0.0417 * sueldo_sin_extras) + (0.0417 * valor_horas_extras)
    return prima_servicio, cesantias, intereses_cesantias, vacaciones

# para calcular el salario neto 
def sueldo_neto(salud, pension, parafiscales, s_bruto):
    return s_bruto - (parafiscales + salud + pension)

# para imprimir los datos del docente
def imprime_datos():
    print(" ")
    print("\t\t","="*40)
    print("\t\t Datos del Docente".center(40))
    print("\t\t","="*40)
    print("\t\t Nombre del docente       : ",nombre)
    print("\t\t Horas trabajadas         : ", horas_trabajadas)
    print("\t\t Valor de la hora         : ","$",valor_hora)
    print("\t\t","="*40)
    print("\t\t Datos para el sueldo bruto".center(40))
    print("\t\t","="*40)
    print("\t\t Horas extras trabajadas  : ", horas_extras)
    print("\t\t Total pagar las 40 horas : ","$", sueldo_sin_extras)
    print("\t\t Total pagar horas extras : ","$", valor_horas_extras)
    print("\t\t Sueldo bruto a pagar     : ","$", s_bruto)
    print("\t\t","="*40)
    print("\t\t Datos de los descuentos".center(40))
    print("\t\t","="*40)
    print("\t\t Descuento Parafiscales 9% : ","$", round(parafiscales, 3))
    print("\t\t Descuento Salud 4%        : ","$", round(salud, 3))
    print("\t\t Descuento Pension 4%      : ","$", round(pension,3))
    print("\t\t Suma de los descuentos    : ","$", round(suma_descuentos,3))
    print("\t\t","="*40)
    print("\t\t Sueldo Neto a Pagar".center(40))
    print("\t\t","="*40)
    print("\t\t Total sueldo neto a pagar :","$", round(s_neto, 3))
    print("\t\t","="*40)
    print("\t\t Datos de las provisiones ".center(40))
    print("\t\t","="*40)
    print("\t\t Provision por prima       : ","$", round(prima_servicio, 3))
    print("\t\t Provision por cesantias   : ","$", round(cesantias, 3))
    print("\t\t Provision por I. cesantias: ","$", round(intereses_cesantias, 3))
    print("\t\t Provision por vacaciones  : ","$", round(vacaciones, 3))
    print("\t\t","="*40)
    print(" ")

#Datos de totales 
def datos_globales():
    print(" ")
    print("\t","="*46)
    print("\t El TOTAL acumulado de los sueldos ".center(46))
    print("\t","="*46)
    print("\t Cantidad de docentes procesados  : ", docentes)
    print("\t","="*46)
    print("\t Acumulado total del sueldo bruto : ","$", round(total_bruto,3))
    print("\t Acumulado total del sueldo neto  : ","$", round(total_neto, 3))
    print("\t","="*46)
    print(" ")
    input("Pulse ENTER para salir.......")


nombre = " "
horas_trabajadas = valor_hora = horas_extras = sueldo_sin_extras = docentes = 0
s_bruto = valor_horas_extras = parafiscales = salud = pension = prima_servicio = cesantias = intereses_cesantias = vacaciones = s_neto = 0.0
total_neto = total_bruto = suma_descuentos = 0.0

while True:
    print("\t","="*57)
    print("\t Programa para calcular las ganacias de un docente".center(56))
    print("\t Si desea salir del programa escriba como NOMBRE salir".center(56))
    print("\t","="*57)
    #creo un condicional para salirme del bucle while
    nombre = input("\t Ingrese el nombre del docente: ").upper()
    if nombre == "SALIR":
        break

    #Contador para saber la cantidad de docentes procesados 
    docentes += 1

    # hago un ciclo while para validar que ingresen valores coherentes para las horas trabajadas y el valor de la hora.    
    horas_trabajadas = int(input("\t Ingrese la cantidad de horas trabajadas por el docente: "))
    while True:
        #coloco este condicional porque se evaluan las horas trabajadas semanalmente
        if horas_trabajadas >= 0 and horas_trabajadas <= 168:
            break
        else:
            horas_trabajadas = int(input("\t Las horas trabajadas estan establecidas entre 0 y 168, por favor ingresela nuevamente: "))
    
    valor_hora = int(input("\t Ingrese el valor a pagar por hora trabajada: "))
    while True:
        if valor_hora >= 0:
            break
        else:
            valor_hora = int(input("\t El precio de la hora debe ser mayor a cero, por favor ingreselo nuevamente: "))
    
    #llamo a las funcuines
    s_bruto, horas_extras, valor_horas_extras, sueldo_sin_extras = sueldo_bruto(valor_hora, horas_trabajadas)
    parafiscales, salud, pension, suma_descuentos = descuentos(s_bruto)
    s_neto = sueldo_neto(salud, pension, parafiscales, s_bruto)
    prima_servicio, cesantias, intereses_cesantias, vacaciones = provisiones(sueldo_sin_extras, valor_horas_extras)

    # acumuladores para saber el total final del sueldo bruto y neto de todos los docentes procesados.
    total_bruto += s_bruto
    total_neto += s_neto

    imprime_datos()
   
datos_globales()





