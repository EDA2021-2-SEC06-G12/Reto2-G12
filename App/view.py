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
import time
assert cf

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

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
        print("Catálogo Inicializado")
    
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont)
        print('Artistas cargados: ' + str(controller.artistSize(cont)))
        print('Obras de Arte cargadas: ' + str(controller.artworkSize(cont)))
    
    elif int(inputs[0]) == 3:
                
        A_I = input("Ingresa el año inicial: ") #1920
        A_FN = input("Ingresa el año final: ") #1985
        start_time = time.process_time()
        lista = controller.listar_artist_date(A_I, A_FN, cont)
<<<<<<< HEAD
        print("Se cargaron un total de", lista[0], "Artistas")
        print("Los primeros 3 artistas son:", lista[1])
        print("Los últimos 3 artistas son:", lista[2])
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))
=======
        print("\nSe cargaron un total de", lista[0], "Artistas\n")
        print("Los primeros 3 artistas son:\n", lista[1])
        print("Los últimos 3 artistas son:\n", lista[2])

>>>>>>> 6f8acadb34c0064e603d7b90e925daef0bdcef1e
    elif int(inputs[0]) == 4:
        
        F_I = input("Ingresa la fecha inicial (AAAA-MM-DD): ") #1944-06-06
        F_FN = input("Ingresa la fecha final (AAAA-MM-DD): ") #1989-11-09
        start_time = time.process_time()
        lista = controller.listar_artwork_date(F_I, F_FN, cont)
<<<<<<< HEAD
        print("Se cargaron un total de", lista[0], "obras, en donde un total de", lista[3], "fueron adquiridas por compra.")
        print("Los primeros 3 artistas son:", lista[1])
        print("Los últimos 3 artistas son:", lista[2])
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))
=======
        print("\nSe cargaron un total de", lista[0], "obras, en donde un total de", lista[3], "fueron adquiridas por compra.\n")
        print("Las primeras 3 obras son:\n", lista[1])
        print("Las últimas 3 obras son:\n", lista[2])
>>>>>>> 6f8acadb34c0064e603d7b90e925daef0bdcef1e

    elif int(inputs[0]) == 5:
        Name = input("Ingresa el nombre del artista: ") #Louise Bourgeois
        start_time = time.process_time()
        lista = controller.clasificacion_medio_t_obra(Name, cont)
<<<<<<< HEAD
        print("El total de obras es: " + str(lista[0]))
        print("El total de técnicas es: " + str(lista[1]))
        print("El nombre de la técnica más usada es: " + str(lista[2]))
        print("Las primeras 3 obras dentro de la técnica más utilizada son:", lista[4])
        print("Las últimas 3 obras dentro de la técnica más utilizada son:", lista[5])
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))

=======
        print("\nEl total de obras es:\n", str(lista[0]))
        print("El total de técnicas es:\n", str(lista[1]))
        print("El nombre de la técnica más usada es:\n", str(lista[2]))
        print("Las primeras 3 obras dentro de la técnica más utilizada son:\n", lista[4])
        print("Las últimas 3 obras dentro de la técnica más utilizada son:\n", lista[5])
        
>>>>>>> 6f8acadb34c0064e603d7b90e925daef0bdcef1e
    elif int(inputs[0]) == 6:
        start_time = time.process_time()
        print("Obras por la nacionalidad de sus creadores: ")
        lista = controller.Obras_Nacionalidad(cont)
<<<<<<< HEAD
        print("El top 10 de nacionalidades son:", lista[0])
        print("Las primeras 3 obras dentro de la mayor nacionalidad son:", lista[1])
        print("Las últimas 3 obras dentro de la mayor nacionalidad son:", lista[2])
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))

=======
        print("\nEl top 10 de nacionalidades son:\n", lista[0])
        print("Las primeras 3 obras dentro de la mayor nacionalidad son:\n", lista[1])
        print("Las últimas 3 obras dentro de la mayor nacionalidad son:\n", lista[2])
    
>>>>>>> 6f8acadb34c0064e603d7b90e925daef0bdcef1e
    elif int(inputs[0]) == 7:
        department = input ("Ingresa el nombre del departamento a buscar: ") #Drawings & Prints
        start_time = time.process_time()
        lista = controller.Costo_departamento(department, cont)
<<<<<<< HEAD
        print("El número total de obras a transportar es", lista[0])
        print("El costo total es de", lista[1], "USD aproximadamente.")
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El tiempo de ejecución es (mseg): ' + str(elapsed_time_mseg))

=======
        print("\nEl número total de obras a transportar es\n", lista[0])
        print("El costo total es de", lista[1], "USD aproximadamente.\n")
        print("Las 5 obras más antiguas a transportar son:\n", lista[2])
        print("Las 5 obras más costosas a transportar son:\n", lista[3])
    
>>>>>>> 6f8acadb34c0064e603d7b90e925daef0bdcef1e
    elif int(inputs[0]) == 8:
        num_artistas = input("Ingrese la cantidad de artistas que desea clasificar: ") #7
        A_I = input("Ingresa el año inicial: ") #1914
        A_FN = input("Ingresa el año final: ") #1939
        lista_cronologica = controller.listar_artist_date(A_I, A_FN, cont)
        print("\nSe cargaron un total de", lista_cronologica[0], "Artistas.\n")
        cronologia = lista_cronologica[3]['elements']
        lista = controller.Artista_prolifico(cronologia, num_artistas, cont)
        print(lista)
        
    else:
        sys.exit(0)
sys.exit(0)