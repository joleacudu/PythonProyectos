"""
Autor: Jorge Leonardo Cuellar Dussan 
       C.C 1075258538

Universidad: El Bosque - Grupo 50, Ciclo 1 Fundamentos de programacion.

Fecha: 15/05/2021

Situación

Una Universidad colombiana asesorada por la Universidad El Bosque y siguiendo su mismo espíritu de ayuda a las clases menos favorecidas, ha 
diseñado un esquema de porcentajes de ayuda (descuento sobre la matrícula) para sus nuevos estudiantes que funciona de la siguiente manera:

• Cada estudiante candidato deberá dar su nombre y apellidos, su edad en años, el puntaje obtenido en el examen y el número decimal de salarios
  mínimos mensuales que tiene de ingreso familiar.
• Presentar un examen de aptitud académica y razonamiento, calificado en números enteros de 0 a 100.
• Cálculo del porcentaje de apoyo según los siguientes criterios:
    • Si la edad está en el rango 15 a 18 años dar 25%, de 19 a 21 años dar 15% y de 22 a 25 años dar 10%, para mayores de 25 no dar ningún apoyo 
     por edad.
    • Si el ingreso familiar es inferior o igual a un salario mínimo dar 30%, si es mayor a un salario mínimo e inferior o igual a 2 salarios mínimos
    dar 20%, si es mayor a dos salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%, si es mayor a tres salarios mínimos e inferior o 
    igual a 4 salarios mínimos dar 5%, para ingresos superiores no dar ningún apoyo por ingreso familiar.
    • Si puntaje de ingreso es mayor o igual a 80 y menor de 86 dar 30%, si es mayor o igual a 86 y menor de 91 dar 35%, si es mayor o igual a 91 y
    menor de 96 dar 40%, si es mayor o igual a 96 dar 45%. Para puntajes menores de ochenta no hay apoyo por puntaje de examen.
    • Los apoyos recibidos por edad, por ingreso familiar y por puntaje de examen se deben sumar para dar el porcentaje total de apoyo que recibirá
    el beneficiario, es decir, el porcentaje de descuento sobre el valor de la matrícula.

El dueño de la Universidad le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:

• Leer desde el teclado el nombre y apellido del candidato, su edad entera en años, el puntaje obtenido en el examen y el número decimal de
  salarios mínimos mensuales de su ingreso familiar.
• Calcular el valor total de descuento del candidato según los criterios antes definidos.
• Mostrar en consola el nombre y apellido del beneficiario, el descuento recibido por edad, el recibido por el ingreso familiar, el recibido por
  el puntaje del examen y el descuento total que recibirá sobre el valor de la matrícula.
"""

#Entradas nombre, edad, puntaje, ingreso.
#salidas nombre, descuento por edad, descuento por ingreso, descuento por puntaje, descuento total.

# declaro las variables y las asigno.
nombre=mensaje="" #String
edad=puntaje=descuento_edad=descuento_ingreso=descuento_puntaje=descuento_total=0 #entero (int)
ingreso=0.0 #decimal (float)

#creo un bucle para agregar los datos de varios estudiantes candidatos y no tener que correr el codigo  cada vez que se necesite agregar uno.
while True:

    #ingreso el valor de las variables por consola

#------------------------------------------CODIGO PARA INGRESAR EL NOMBRE--------------------------------------------------------------------------------
    nombre=input("Ingrese los nombres y apellidos del estudiante candidato: ").upper() # Ingreso el nombre por consola

#-------------------------------------------CODIGO PARA INGRESAR LA  EDAD CORRECTA-----------------------------------------------------------------------
    
    edad=int(input("Ingrese la edad en años del estudiante candidato: "))
    while edad<15 or edad>85: #con este while logro que el usuario ingrese una edad mayor a 15 años ya que este es el rango inferior en la edad para los descuentos
        print("\tIngreso una edad incorrecta por favor intentelo nuevamente.")
        edad=int(input("Ingreso una edad entre 15 años y 85 años: "))
    if edad>25: # el descuento para las edades mayores a 25 años
        descuento_edad=0
    elif edad>=22: # el descuento para las edades entre 22 a 25 años
        descuento_edad=10
    elif edad>=19: # el descuento para las edades entre 19 a 21 años
        descuento_edad=15
    elif edad>=15: # el descuento para las edades entre 15 a 18 años
        descuento_edad=25 

#------------------------------CODIGO PARA INGRESAR EL VALOR DEL EXAMEN EN EL RANGO ESTABLECIDO----------------------------------------------------------------------
   
    puntaje=int(input("Ingrese el puntaje del examen de actitud de 0 a 100 del estudiante candidato: "))
    while puntaje<0 or puntaje>100: #con este while evito que ingresen valores menores a cero y generen resultados erroneos.
        print("\tEl puntaje esta establecido entre 0 y 100, ingrese un valor entre este rango por favor.")
        puntaje=int(input("Ingrese el puntaje del examen de actitud de 0 a 100 del estudiante candidato: "))#pido nuevamente el ingreso del dato
    if puntaje>=96: #Descuento por un puntaje mayor o igual a 96
        descuento_puntaje=45
    elif puntaje>=91: #Descuento por un puntaje mayor o igual a 91
        descuento_puntaje=40
    elif puntaje>=86: #Descuento por un puntaje mayor o igual a 86
        descuento_puntaje=35
    elif puntaje>=80: #Descuento por un puntaje mayor o igual a 80
        descuento_puntaje=30
    elif puntaje<80: #Descuento por un puntaje menor a 80
        descuento_puntaje=0

#------------------------------------------------CODIGO PARA INGRESAR UN INGRESO FAMILIAR------------------------------------------------------------------------------

    ingreso=float(input("Ingrese el número decimal de salarios mínimos mensuales que tiene de ingreso familiar: "))
    while ingreso<0: #Este while impide que ingresen valores menores a cero y generen datos falsos.
        print("\tEl ingreso familiar no puede ser menor a cero, por favor ingrese un valor correcto.")
        ingreso=float(input("Ingrese el número decimal de salarios mínimos mensuales que tiene de ingreso familiar: "))#pido nuevamente el valor de la variable ingreso 
    if ingreso>4: #Descuento dado para el ingreso mayor a 4 salarios minimos
        descuento_ingreso=0
    elif ingreso>3: #Descuento dado para el ingreso mayores a 3 e iguales a 4 salarios minimos
        descuento_ingreso=5
    elif ingreso>2: #Descuento dado para el ingreso mayores a 2 e iguales a 3 salarios minimos
        descuento_ingreso=10
    elif ingreso>1: #Descuento dado para el ingreso mayores a 1 e iguales a 2 salarios minimos
        descuento_ingreso=20
    elif ingreso>=0: #Descuento dado para el ingreso entre 0 y 1 salario minimo
        descuento_ingreso=30

#imprimo los datos ingresados mas los obtenidos en una tabla agradable para el usuario
    print("")
    print("\t=======================================================================")
    print("\t                  Datos del Estudiante Candidato")
    print("\t=======================================================================")
    print("\tNombre                            : ",nombre)
    print("")
    print("\tEdad en años                      : ",edad)
    print("\tdescuento por edad                : ",descuento_edad, "%")
    print("")
    print("\tIngreso familiar en decimales     : ",ingreso)
    print("\tdescuento por ingreso familiar    : ",descuento_ingreso, "%")
    print("")
    print("\tPuntaje obtenido en el examen     : ",puntaje)
    print("\tdescuento por puntaje en el examen: ",descuento_puntaje, "%")
    print("\t----------------------------------------------------------------------")
    print("\tdescuento total sobre la matricula: ",descuento_edad + descuento_ingreso + descuento_puntaje,"%")
    print("\t======================================================================")
    print("")
    control=int(input("\tDesea agregar otro empleado, con 1:SI o con 0:SALIR= "))
    if control==0:
        break #con este control lo que se logra es salir del ciclo while.


print("\t Estamos saliendo del programa")
print("\t Pulse una tecla para terminar.")
exit()




