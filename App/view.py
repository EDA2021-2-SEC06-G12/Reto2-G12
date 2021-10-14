"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import model
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Listar cronológicamente los artistas")
    print("4- Listar cronológicamente las adquisiciones")
    print("5- Clasificar las obras de un artista por técnica")
    print("6- Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Transportar obras de un departamento")
    print("8- Encontrar los artistas más prolíficos del museo")
    print("9- Total de obras por una nacionalidad")
    print("0- Salir del Menu")


# Funciones de inicializacion

def initCatalog():
    catalog= model.newcatalog()
    return catalog


def loadData(catalog):
    controller.loadData(catalog)
 
catalog= None




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("Catálogo Inicializado")
        
    
    elif int(inputs[0]) == 2:
        #nacionalidad= input('ingrese la nacionalidad')
        print("Cargando información de los archivos ....")
        #start_time = time.process_time()
        controller.loadData(catalog)
        #stop_time = time.process_time()
        #elapsed_time_mseg = (stop_time - start_time)*1000
        print('Artistas cargados: ' + str(controller.artistSize(catalog)))
        print('Obras de Arte carga1das: ' + str(controller.artworkSize(catalog)))
        #print('Nacionalidades cargadas: ' + str(controller.NationalitySize(cont)))
        #print('las nacionalidades son: ' + str(controller.getnationality(cont)))
        #print('Medios cargados: ' + str(controller.MediumSize(cont)))
        #print('los medios son: ' + str(controller.getmedio(cont)))
        #print('Las fechas cargadas son: '+ str(controller.BeginDateSize(cont)))
        #print('las fechas son: '+ str(controller.getfecha(cont)) )
        #print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))
    
    elif int(inputs[0]) == 3:
        A_I = input ("Ingresa el año inicial: ")
        A_FN = input ("Ingresa el año final: ")
        lista = controller.crono_BeginDate(A_I,A_FN,catalog)
        tamaño = lt.size(lista)
        print ("Se cargaron un total de", tamaño, "Artistas")
        print ("Los primeros 3 artistas son:" , lista[0],lista[1],lista[2])
        print ("Los últimos 3 artistas son:" , lista[len(lista)-1],lista[len(lista)-2],lista[len(lista)-3])

    elif int(inputs[0]) == 4:
        F_I = input ("Ingresa la fecha inicial (AAAA-MM-DD): ")
        F_FN = input ("Ingresa la fecha final (AAAA-MM-DD): ")

    elif int(inputs[0]) == 5:
        Name = input ("Ingresa el nombre del artista: ")
        print('El total de obras y sus primeras y ultimas son:'+ str(controller.clasificacion_medio_t_obra(catalog,Name)))
    elif int(inputs[0]) == 6:
        print("Obras por la nacionalidad de sus creadores: ")
    
    elif int(inputs[0]) == 7:
        print("Transportar obras de un departamento: ")
    
    elif int(inputs[0]) == 8:
        print("Encontrar los artistas más prolíficos del museo: ")
    elif int(inputs[0]) == 9:
        nacionalidad= input("ingrese la nacionalidad: ")
        #print('El total de obras de esa nacionalidad es : ' + str(controller.T_obras_nacionalidad(nacionalidad,catalog)))    
        print('el total de las obras son: ' + str(controller.T_obras_nacionalidad (nacionalidad,catalog)))
    else:
        sys.exit(0)
sys.exit(0)
