import json
import os

lista_de_pinturas = []
lista_de_cotas = []


# Descarga la lista que esta en el archivo data.txt


def descargar_lista_de_pinturas():
    if(os.path.exists("Datos.txt") and os.stat("Datos.txt").st_size != 0):
        with open('Datos.txt') as json_file:
            data = json.load(json_file)
            return data
    return []


lista_de_pinturas = descargar_lista_de_pinturas()
if(len(lista_de_pinturas) > 0):
    for i in range(len(lista_de_pinturas)):
        lista_de_cotas.append(
            {"posicion": i, "cota": lista_de_pinturas[i]["serial"]})
        lista_nombre = lista_de_pinturas[i]["nombre"].split(" ")
        
        

def crear_pintura(lista_de_pinturas,lista_de_cotas):

    print("Para ingresar una pintura se requiere que ingrese los valores de la cota,Nombre,Precio y Status")

    while True:
        cota = input("Ingrese la Cota de la puintura (Debe poseer 4 letras y 4 digitos (Ejemplo ABCD123")
        if len(cota)==8:
            contador1 = 0
            contador2 = 0
            for letra in cota:
                if letra.isnumeric():
                    contador1 +=1
                elif letra.isalpha():
                    contador2 +=1
            if contador1 == 4 and contador2 == 4:
                break
            else:
                print("Error! No es un Serial valido")
        else:
            print("Error! No tiene 8 caracteres")

    while True:
        nombre = input('Ingrese el nombre de la obra. Puede contener maximo 30 caracteres')
        if len(nombre) < 30 and len(nombre)> 0:
            break
        else:
            print("Ingrese un nombre valido")

    while True:
        try:
            precio = int(input('Ingrese el precio de la obra'))
            break
        except:
            print('Ingrese un precio valido')

    while True:
        status = input('Ingrese 1 si la obra esta en En exhibicion, ingrese 2 si esta En mantenimiento\n ')
        if status == '1':
            status =  "EN EXHIBICIÓN"
            break
        elif status == '2':
            status = "EN MANTENIMIENTO"
            break
        else: 
            print('Ingrese una opcion valida')





def inicio(lista_de_pinturas, lista_de_cotas):
    # Mensaje de bienvenida con las posibles opciones.
    print("""
    Opciones de la aplicación:

    1. Insertar nueva pintura.
    2. Consulta de una pintura.
    3. Puesta en exhibicion.
    4. Eliminacion.
    5. Borrar Pintura.
    6. Compactador.
    7. Salir.
    """)


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
inicio(lista_de_pinturas, lista_de_cotas)
