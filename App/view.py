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
    print("0- Salir del Menu")


# Funciones de inicializacion

def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        print("Catálogo Inicializado")
        cont = controller.initCatalog()
    
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        start_time = time.process_time()
        controller.loadData(cont)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('Artistas cargados: ' + str(controller.artistSize(cont)))
        print('Obras de Arte cargadas: ' + str(controller.artworkSize(cont)))
        print('Nacionalidades cargadas: ' + str(controller.NationalitySize(cont)))
        print('Medios cargados: ' + str(controller.MediumSize(cont)))
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))
    
    elif int(inputs[0]) == 3:
        A_I = input ("Ingresa el año inicial: ")
        A_FN = input ("Ingresa el año final: ")

    elif int(inputs[0]) == 4:
        F_I = input ("Ingresa la fecha inicial (AAAA-MM-DD): ")
        F_FN = input ("Ingresa la fecha final (AAAA-MM-DD): ")

    elif int(inputs[0]) == 5:
        Name = input ("Ingresa el nombre del artista: ")
        
    elif int(inputs[0]) == 6:
        print("Obras por la nacionalidad de sus creadores: ")
    
    elif int(inputs[0]) == 7:
        print("Transportar obras de un departamento: ")
    
    elif int(inputs[0]) == 8:
        print("Encontrar los artistas más prolíficos del museo: ")
        

    else:
        sys.exit(0)
sys.exit(0)
