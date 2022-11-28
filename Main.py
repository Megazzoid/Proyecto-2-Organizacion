import json
import os

lista_de_pinturas = []
indice_cotas = []
indices_nombres = []


# Descarga la lista que esta en el archivo data.txt


def descargar_lista_de_pinturas():
    if(os.path.exists("Datos.txt") and os.stat("Datos.txt").st_size != 0):
        with open('Datos.txt') as json_file:
            data = json.load(json_file)
            return data
    return []


lista_de_pinturas = descargar_lista_de_pinturas()
   
def actualizar_lista_de_pinturas(lista_nueva):
    with open('Datos.txt', 'w') as outfile:
        json.dump(lista_nueva, outfile)    
        

def crear_pintura(lista_de_pinturas):

    print("Para ingresar una pintura se requiere que ingrese los valores de la cota, Nombre, Precio y Status")

    continuar = True
    while continuar:
        cota = input("Ingrese la Cota de la pintura (Debe poseer 4 letras y 4 digitos (Ejemplo ABCD123): ")
        if len(cota)==8:
            contador1 = 0
            contador2 = 0
            for letra in cota:
                if letra.isnumeric():
                    contador1 +=1
                elif letra.isalpha():
                    contador2 +=1
            if contador1 == 4 and contador2 == 4:
                for element in indice_cotas:
                    if cota == element['cota']:
                        print('La cota ya existe')
                        crear_pintura(lista_de_pinturas)
                    else:
                        continuar = False
            else:
                print("Error! No es un Serial valido")
        else:
            print("Error! No tiene 8 caracteres")

    while True:
        nombre = input('Ingrese el nombre de la obra. Puede contener maximo 30 caracteres: ')
        if len(nombre) < 30 and len(nombre)> 0:
            break
        else:
            print("Ingrese un nombre valido")

    while True:
        try:
            precio = int(input('Ingrese el precio de la obra: '))
            if precio > 0:
                break
            else:
                print('Ingrese un precio valido')
        except:
            print('Ingrese un precio valido')

    while True:
        status = input('Ingrese 1 si la obra esta en En exhibicion, ingrese 2 si esta En mantenimiento\n ')
        if status == '1':
            status =  "EN EXHIBICION"
            break
        elif status == '2':
            status = "EN MANTENIMIENTO"
            break
        else: 
            print('Ingrese una opcion valida')

    pintura = {
        "cota":cota,
        "nombre":nombre,
        "Precio":precio,
        "Status":status,
        "Existencia":True
    }

    lista_de_pinturas.append(pintura)

    actualizar_lista_de_pinturas(lista_de_pinturas)

    inicio()

def PonerMantenimientoCota():
    cota = input('Ingrese a la cota que desea buscar:')

    contador = 0
    
    for element in indice_cotas:
        if cota == element['cota']:

            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == True:
                if lista_de_pinturas[posicion]['Status'] == 'EN MANTENIMIENTO':
                    print('La obra ya esta en mantenimiento\n')
                    inicio()
                else:
                    lista_de_pinturas[posicion]['Status'] = 'EN MANTENIMIENTO'
                    print('La obra acaba de ser puesta en mantenimiento\n')
                    actualizar_lista_de_pinturas(lista_de_pinturas)
                    inicio()
            else:
                print('La cota no existe')
                inicio()

        else:
            pass

    print('No existe ninguna obra con la cota que ingreso')    
    inicio()
    
    
def PonerMantenimientoNombre():
    nombre = input('Ingrese el nombre de la obra que desea buscar:')

    for element in indices_nombres:
        if nombre == element['nombre']:

            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == True:
                if lista_de_pinturas[posicion]['Status'] == 'EN MANTENIMIENTO':
                    print('La obra ya esta en mantenimiento\n')
                    inicio()
                else:
                    lista_de_pinturas[posicion]['Status'] = 'EN MANTENIMIENTO'
                    print('La obra acaba de ser puesta en mantenimiento\n')
                    actualizar_lista_de_pinturas(lista_de_pinturas)
                    inicio()
            else:
                print('La obra con el nombre que ingreso no existe')
                inicio()
            
        else:
            pass

    print('No existe ninguna obra con el nombre que ingreso')    
    inicio()


def PonerMantenimiento():

    opcion = input("""
    Indique como quiere buscar la pintura:
    1-Por Cota
    2-Por nombre 
    """)
    
    if opcion == '1':
        PonerMantenimientoCota()
    elif opcion == '2':
        PonerMantenimientoNombre()
    else:
        print('Ingreso una opcion equivocada') 
        PonerMantenimiento()

def PonerExhibicionCota():
    cota = input('Ingrese a la cota que desea buscar:')

    

    for element in indice_cotas:
        if cota == element['cota']:

            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == True:
                if lista_de_pinturas[posicion]['Status'] == 'EN EXHIBICION':
                    print('La obra ya esta en Exhibicion\n')
                    inicio()
                else:
                    lista_de_pinturas[posicion]['Status'] = 'EN EXHIBICION'
                    print('La obra acaba de ser puesta en enxihibicion\n')
                    actualizar_lista_de_pinturas(lista_de_pinturas)
                    inicio()
            else:
                print('La cota no existe')
                inicio()
            
        else:
            pass

    print('No existe ninguna obra con la cota que ingreso')    
    inicio()

def PonerExhibicionNombre():
    nombre = input('Ingrese a la cota que desea buscar:')

    

    for element in indices_nombres:
        if nombre == element['nombre']:

            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == True:
                if lista_de_pinturas[posicion]['Status'] == 'EN EXHIBICION':
                    print('La obra ya esta en exhibicion\n')
                    inicio()
                else:
                    lista_de_pinturas[posicion]['Status'] = 'EN EXHIBICION'
                    print('La obra acaba de ser puesta en exhibicion\n')
                    actualizar_lista_de_pinturas(lista_de_pinturas)
                    inicio()
            else:
                print('La obra con el nombre que ingreso no existe')
                inicio()
            
        else:
            pass

    print('No existe ninguna obra con la cota que ingreso')    
    inicio()
def PonerExhibicion():

    opcion = input("""
    Indique como quiere buscar la pintura:
    1-Por Cota
    2-Por nombre 
    """)
    
    if opcion == '1':
        PonerExhibicionCota()
    elif opcion == '2':
        PonerExhibicionNombre()
    else:
        print('Ingreso una opcion equivocada') 
        PonerExhibicion()

def eliminar():
    
    opcion = input("""
    Indique como quiere buscar la pintura que quiere eliminar:
    1-Por Cota
    2-Por nombre 
    """)

    if opcion == '1':
        eliminarporcota()
    elif opcion == '2':
        eliminarpornombre()
    else:
        print('Ingreso una opcion equivocada') 
        eliminar()  

def eliminarporcota():

    cota = input('Ingrese la cota que desea eliminar:')

    for element in indice_cotas:
        if cota == element['cota']:
            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == False:
                print('No existe la cota que desea eliminar')
                inicio()
            else:
                lista_de_pinturas[posicion]['Existencia'] = False
                print('Se ha eliminado con exito la cota')
                inicio()            
        else:
            pass
    
    print('No exista la cota que desea eliminar')
    inicio()

def eliminarpornombre():
    
    nombre = input('Ingrese la cota que desea eliminar:')

    for element in indices_nombres:
        if nombre == element['nombre']:
            posicion = element['posicion']
            if lista_de_pinturas[posicion]['Existencia'] == False:
                print('No existe la cota que desea eliminar')
                inicio()
            else:
                lista_de_pinturas[posicion]['Existencia'] = False
                print('Se ha eliminado con exito la cota')  
                inicio()          
        else:
            pass
    
    print('No exista la cota que desea eliminar')


def Compactador():
    print('El proceso de Compactor ha comenzado ')

    listaeliminar = []

    for x in range(0,len(lista_de_pinturas)):
        if lista_de_pinturas[x]['Existencia'] == False:
            listaeliminar.append(x)

    listaeliminar.sort(reverse=True) 

    for x in listaeliminar:
        lista_de_pinturas.pop(x)

    actualizar_lista_de_pinturas(lista_de_pinturas) 

    print('Se actualizo fisicamente')

    inicio()


def inicio():

    indice_cotas.clear()
    indices_nombres.clear()

    for i in range(len(lista_de_pinturas)):
        indice_cotas.append(
            {"posicion": i, "cota": lista_de_pinturas[i]["cota"]})
        indices_nombres.append(
            {"posicion": i, "nombre": lista_de_pinturas[i]["nombre"]})


    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Opciones de la aplicación:

    1. Insertar nueva pintura.
    2. Poner en mantenimiento.
    3. Poner en exhibicion.
    4. Borrar Pintura.
    5. Compactador.
    6. Salir.
    """)

    opcion = input('Ingrese su opcion')

    if opcion == '1':
        crear_pintura(lista_de_pinturas)
    elif opcion == '2':
        PonerMantenimiento()
    elif opcion == '3':
        PonerExhibicion()
    elif opcion == '4':
        eliminar()
    elif opcion == '5':
        Compactador()
    elif opcion == '6':
        exit()
    else:
        print('Ingreso una opcion no valida')
        inicio()

# Mensaje de Bienvenida
print(""" 

██╗      ██████╗ ██╗   ██╗██╗   ██╗██████╗ ███████╗
██║     ██╔═══██╗██║   ██║██║   ██║██╔══██╗██╔════╝
██║     ██║   ██║██║   ██║██║   ██║██████╔╝█████╗  
██║     ██║   ██║██║   ██║╚██╗ ██╔╝██╔══██╗██╔══╝  
███████╗╚██████╔╝╚██████╔╝ ╚████╔╝ ██║  ██║███████╗
╚══════╝ ╚═════╝  ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝
                                                   
 \nBienvenido Gestión de Pinturas para el Louvre.
 """)



inicio()
