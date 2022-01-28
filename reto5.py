"""
Autor: Jorge Leonardo Cuellar Dussan 1075258538

El director del Programa de Ingeniería de Sistemas de la Universidad El Bosque, a raíz de la participación en un proyecto muy especial con el 
MinTic, requiere poder generar una agenda con los datos de nombre y apellido, número de cédula y el número celular de todos los beneficiarios 
del proyecto, para poder hacerles algún seguimiento en su proceso de formación. Dicha agenda deberá ser almacenada en un archivo de texto en 
el directorio activo con el nombre agenda.txt. Cada beneficiario ocupará tres líneas en el archivo, una por cada campo (nombre y apellido, 
cedula, celular). Por ejemplo, el beneficiario José Castro con cédula 18145321 y celular 3091234567 y la beneficiaria Sofía Vergara con cédula 
52120318 y celular 3109876543, quedarían así en el archivo:

José Castro
18145321
3091234567
Sofía Vergara
52120318
3109876543

El director del Programa de Ingeniería de Sistemas le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python
que le permita:

• Crear el archivo agenda.txt leyendo los datos desde el teclado (por lo menos 10 beneficiarios).
• Buscar en el archivo agenda.txt el número celular de un beneficiario, dados su nombre y apellido.
• Añadir un nuevo beneficiario en la agenda.txt, al final del archivo. No debe haber otro beneficiario con la misma cédula.
• Borrar un beneficiario de la agenda.txt dado su número de cédula.
• Buscar, añadir y borrar un beneficiario deberán ser funciones, que serán llamadas dentro del programa principal.
• Mostrar en consola el listado completo de los beneficiarios del archivo agenda.txt.
• Mostrar en consola el listado de los beneficiarios cuyo nombre empieza por una letra determinada.
• Presentar un menú con las diferentes opciones solicitadas para que el usuario pueda decidir qué proceso desea realizar.
"""

def menu():
    import os
    opcion = 0
    os.system('cls')
    while True:
        os.system('cls')
        print("\t","="*40)
        print("\t","Menu Pricipal".center(40))
        print("\t","="*40)
        print("\t\t1. Ver listado")
        print("\t\t2. Ver listado filtrado")
        print("\t\t3. Agregar beneficiario")
        print("\t\t4. Buscar beneficiario")
        print("\t\t5. Borrar beneficiario")
        print("\t\t6. Salir")
        print("\t","="*40)
    
        opcion = int(input("\t Elije la opción: "))
        if opcion == 1:
            listado()
        elif opcion == 2:
            listado_modificado()
        elif opcion == 3:
            añadir()
        elif opcion == 4:
            buscar()
        elif opcion == 5:
            borrar()
        elif opcion == 6:
            print(" ")
            print("\t","="*55)
            print("\t Reto final del CICLO 1 de FUNDAMENTOS DE PROGRAMACION.")
            print("\t Hasta pronto!!!".center(55))
            print("\t","="*55)
            break
        else:
            print("\t Opción inválida. Reintente")
            pausateclado()

#------------------------------------------muestra el listado de los usuarios-------------------------------------------------------------
def listado():
    #print(datos)
    print("\t","="*70)
    print("\t","Cantidad de usuarios agregados: ",len(datos))
    print("\t","="*70)
    print("\t No               Nombre                 Cedula             Celular")
    print("\t","="*70)
    i = 1
    for dato in datos:
        print("\t",repr(i).ljust(3)," ",repr(dato[0]).ljust(30)," ",repr(dato[1]).ljust(15)," ",repr(dato[2]).ljust(15))
        i += 1
    print("\t","="*70)
    pausateclado()

#-----------------------------------------muestra los usuarios que inicien con la misma letra-------------------------------------------------
def listado_modificado():
    largo = 0
    consulta = input("\t Por favor escriba la letra por la cual quieres hacer la consulta: ")
    print("\t","="*70)
    print("\t","Listado de la informacion del Usuario.".center(70))
    print("\t","Cantidad de Usuarios: ",len(datos))
    print("\t","="*70)
    print("\t No               Nombre                 Cedula             Celular")
    print("\t","="*70)
    i = 1
    for dato in datos:
        nombre = dato[0]
        largo = len(nombre)
        if nombre[0] == consulta:
            print("\t",repr(i).ljust(3)," ",repr(dato[0]).ljust(30)," ",repr(dato[1]).ljust(15)," ",repr(dato[2]).ljust(15))
        i += 1 
          
    print("\t","="*70)
    pausateclado()

#----------------------------------------------------agrega usuarios al archivo------------------------------------------------------------
def añadir():
    cedula = celular = i = 0
    encontrado = False
    nombre = " "
    print("\t Digite la información del beneficiario a agregar:")
    print(" ")
    i = len(datos)
    cedula = int(input("\t Por favor escriba la cedula del usuario a agregar: "))
    while cedula <= 0: 
        cedula = int(input("\t Por favor escriba una cedula correcta: "))
    for dato in datos:
        if cedula == dato[1]:
            encontrado = True
            nombre = dato[0]
    if encontrado: 
        print("\t","="*70)
        print("\t El usuario con cedula ", cedula, " y de nombre ", nombre)
        print("\t No se puede crear porque ya existe en la base de datos")
        print("\t","="*70)
        pausateclado()
        menu()
    else:
        datos.append([])
        nombre = input("\t Por favor escriba el nombre del usuario a agregar: ")
        datos[i].append(nombre)
        datos[i].append(cedula)
        celular = int(input("\t Por favor escriba la celular del usuario a agregar: "))
        while celular <= 0: 
            celular = int(input("\t Por favor escriba un numero de celular correcto: "))
        datos[i].append(celular)
        archivo = open("agenda.txt","a")
        archivo.write(str(nombre))
        archivo.write("\n")
        archivo.write(str(cedula))
        archivo.write("\n")
        archivo.write(str(celular))
        archivo.write("\n")
        archivo.close()
    print(" ")
    print("\t El beneficiario ha sido agregado")
    pausateclado()

#------------------------------------------------busca un usuario dando su nombre completo------------------------------------------------------
def buscar():
    consulta = nom = ""
    ced = cel = 0
    indice = 1
    consulta = input("\t Digite el nombre y apellido del beneficiario a buscar:")
    encontrado = False
    for dato in datos:
        nombre = dato[0]
        if nombre == consulta: 
            encontrado = True
            nom = dato[0] 
            ced = dato[1] 
            cel = dato[2] 
            break
        indice += 1
    if encontrado: 
        print(" ")
        print("\t","="*40)
        print("\t","Datos del Usuario".center(40))
        print("\t","="*40)
        print("\t Indice  :", indice)
        print("\t Nombre  :", nom)
        print("\t Cedula  :", ced)
        print("\t Celular :", cel)
        print("\t","="*40)
        pausateclado()
    else:
        print(" ")
        print("\t","="*60)
        print("\t El usuario con el nombre ", consulta)
        print("\t No se puede encontrar o no existe en la lista.")
        print("\t","="*60)
        pausateclado()   

#-------------------------------------------------borro un usuario dando la cedula------------------------------------------------------------
def borrar():
    cedula = celular = 0
    nombre = " "
    encontrado = False
    cedula = int(input("\t Digite la cedula del beneficiario a borrar:"))
    indice = 0
    for dato in datos:
        if cedula == dato[1]:
            indice_encontrado = indice
            encontrado = True
            nombre = dato[0]
            celular = dato[2]
        indice += 1
    if encontrado: 
        print(" ")   
        print("\t","="*40)
        print("\t","Datos del Usuario".center(40))
        print("\t","="*40)
        print("\t Indice  :", indice_encontrado+1)
        print("\t Nombre  :", nombre)
        print("\t Cedula  :", cedula)
        print("\t Celular :", celular)
        print("\t","="*40)
        while True:
            validar = 0
            print(" ")   
            print("\t","="*40)
            print("\t","¿Seguro que desea borrar este usuario?".center(40))
            print("\t","="*40)
            print("\t\t 1. Borrar")
            print("\t\t 2. Cancelar")
            print("\t","="*40)
            validar = int(input("\t Elija la opcion a realizar: "))
            if validar == 1:
                del(datos[indice_encontrado])
                #datos.pop(indice_encontrado)
                crearArchivo()   
                print(" ")   
                print("\t El usuario ha sido eliminado del listado")   
                pausateclado()    
                break
            elif validar == 2:
                print(" ")   
                print("\t Cancelaste el Borrado")
                pausateclado()    
                break
            else:
                print(" ")   
                print("\t Opción incorrecta. Intentalo nuevanente.")
                print("\t 1. Para borrar o 2. Para salir.")
                pausateclado()    
    else:
        print(" ")
        print("\t No se encontro el Usuario y el registro no se pudo borrar, intentelonuevamente.")
        pausateclado() 

#################################################################################################################################################
#------------------------------------------------------------------otras funciones-----------------------------------------------------------------

#------------------------------------------------------crea el archivo en este caso uno tipo texto------------------------------------------------  
#Se ejecuta durante la ejecucion del codigo, el la parte de borrar usuario para reescribir el archivo con los nuevos datos.
def crearArchivo():
    archivo = open("agenda.txt","w")
    for dato in datos:
        archivo.write(str(dato[0]))
        archivo.write("\n")
        archivo.write(str(dato[1]))
        archivo.write("\n")
        archivo.write(str(dato[2]))
        archivo.write("\n")
    archivo.close()

#-----------------------------------------------------cargo la informacion del archivo---------------------------------------------------------------
#Se ejecuata al correr el codigo, para cargar los datos en dicha variable para poder acceder a ellos desde el primer momento.
def cargarArchivo():
    global datos
    datos = []
    archivo = open("agenda.txt", "a") #para crear el archivo agenda cuando se arranca el codigo por primera vez y dan la opcion 1 en menu no salga error
    cedula = celular = 0
    nombre = " "
    datos.clear() 
    archivo = open("agenda.txt", "r")
    lineas = archivo.readlines() 
    lista = list(lineas)
    j = 0 
    k = 0 
    for i in range(len(lista)): 
        if j == 0: 
            datos.append([])
            nombre = lista[i]
            largo = len(nombre)
            nombre = str(nombre[0:largo-1]) 
            datos[k].append(nombre)
        elif j == 1: 
            cedula = lista[i]
            cedula = int(cedula)
            datos[k].append(cedula)
        elif j == 2: 
            celular = lista[i]
            celular = int(celular)
            datos[k].append(celular)
            j = -1 
            k += 1 
        j += 1
        i += 1 
    
    archivo.close()
    archivo.close()

#---------------------------------------------------------para bloquear la pantalla hasta dar enter---------------------------------------------------------
#Se ejecuta durante la llamada a las funciones por medio del menu para poner una pausa en la pantalla y el usuario pueda leer los mensajes de informacion.
def pausateclado():
    input("\t Pulse ENTER para continuar por favor...")

##################################################################################################################################################################
#--------------------------------llamo a las funciones principales para correr correctamente el codigo-----------------------------------------------------------
cargarArchivo()
menu()

