"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import newList
from DISClib.Algorithms.Sorting import mergesort as mrgs
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {'artist': None,
                'artworks': None,
                'artworkmedium': None,
                'artistNationality': None}
    
    catalog['artist'] = lt.newList('ARRAY_LIST', compareConstituentID)
    catalog['artworks'] = lt.newList('ARRAY_LIST', compareObjectID)

    '''
    Este indice crea un map cuya llave es el medio de una obra
    '''

    catalog['artworkmedium'] = mp.newMap(815,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparenationality)
    
    '''
    Este indice crea un map cuya llave es la nacionalidad de un artista
    '''

    catalog['artistNationality'] = mp.newMap(840,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparemedio)
    catalog['BeginDate']  = mp.newMap(840,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)                                
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    addN_fecha(catalog)

def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    addNationality(catalog)
    addMediums(catalog)


def addMediums(catalog):
    
    for obra in catalog['artworks']['elements']:
        medio = obra['Medium']
        OBJID = obra['ObjectID']
        mp.put(catalog['artworkmedium'], medio, OBJID)

def addNationality(catalog):
    lst = lt.newList('ARRAY_LIST')
    for artista in (catalog['artist']['elements']):
        n= artista['Nationality']
        o=artista['ConstituentID']
        for obra in catalog['artworks']['elements']:
                coids= obra['ConstituentID']
                if o in coids:
                    objectID=obra['ObjectID']
                    lt.addLast(lst, objectID)
                    mp.put(catalog['artistNationality'],n,lst)
            

def lista_obrN(catalog):
    lst = lt.newList('ARRAY_LIST')
    for artista in (catalog['artist']['elements']):
        n= artista['Nationality']
        o=artista['ConstituentID']
    for obra in catalog['artworks']['elements']:
            coids= obra['ConstituentID']
            if o in coids:
                objectID=obra['ObjectID']
                lt.addLast(lst, objectID)
                mp.put(catalog['artistNationality'],n,lst)

def addN_fecha(catalog):
    for artista in catalog['artist']['elements']:
        fecha =  artista['BeginDate']
        name =  artista['DisplayName']
        mp.put(catalog['BeginDate'], fecha, name)

# Funciones para creacion de datos
def newnacionalidad(nacionalidad):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    
    nacionalidad = autor 
    obras =libros
    """
    nationality = {'Nationality': "",
              "artwork": None,
              }
    nationality['Nationality'] = nacionalidad
    nationality['artwork'] = lt.newList('SINGLE_LINKED', comparenationality)

    return nationality


def newmedio(medio):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.

    nacionalidad = autor 
    obras =libros
    """
    medium = {'Medium': "",
              "artwork": None,
              }
    medium['Medium'] = medio
    medium['artwork'] = lt.newList('SINGLE_LINKED', comparemedio)

    return medium

# Funciones de consulta
#    REQUERIMIENTO 1(PRUEBA)
def CRONO (A_I, A_FN,catalog):
    lst_fecha = lt.newList('ARRAY_LIST')

    fechas_llave= mp.keySet(catalog['BeginDate'])
    name_value= mp.valueSet(catalog['BeginDate'])
    for fecha in fechas_llave:
        if (fecha >= A_I) and (fecha <= A_FN):
            for artist in catalog["artist"]["elements"]:
                for name in name_value:
                    if name in artist["DisplayName"]:
                        datos_artist = [artist['DisplayName'], artist['BeginDate'], artist['EndDate'], artist['Nationality'], artist['Gender']]
                        lt.addLast(lst_fecha , datos_artist)

    return lst_fecha

def crono_BeginDate(A_I, A_FN,catalog):
    lst_fecha = lt.newList('ARRAY_LIST')
    fechas_llave = getfecha(catalog)
    orden = ordenamiento_Ndate(fechas_llave)
    for fecha in orden:
        if (fecha >= A_I) and (fecha <= A_FN):
            name= mp.get(catalog['BeginDate'], fecha)
            for artist in catalog["artist"]["elements"]:
                if name in artist["DisplayName"]:
                        datos_artist = [artist['DisplayName'], artist['BeginDate'], artist['EndDate'], artist['Nationality'], artist['Gender']]
                        lt.addLast(lst_fecha, datos_artist)
    return lst_fecha

def T_obras_nacionalidad (nacionalidad,catalog):
    
    return mp.get(catalog['artistNationality'],nacionalidad)
    

def artistSize(catalog):
    """
    Número de artistas en el catálogo
    """
    return lt.size(catalog['artist'])

def artworkSize(catalog):
    """
    Número de obras de arte en el catálogo
    """
    return lt.size(catalog['artworks'])

def NationalitySize(catalog):
    """
    Número de Nacionalidades en el catálogo
    """
    return mp.size(catalog['artistNationality'])

def MediumSize(catalog):
    """
    Número de Medios en el catálogo
    """
    return mp.size(catalog['artworkmedium'])

def BeginDateSize(catalog):
    """
    Número de Medios en el catálogo
    """
    return mp.size(catalog['BeginDate'])    

# Funciones utilizadas para comparar elementos dentro de una lista


# Funciones de comparación

def compareConstituentID(C1, C2):
    '''
    Función de comparación para la lista de artistas (Carga de Datos)
    '''
    if (C1 == C2):
        return 0
    elif (C1 > C2):
        return 1
    else:
        return -1

def compareObjectID(O1, O2):
    '''
    Función de comparación para la lista de obras (Carga de Datos)
    '''
    if (O1 == O2):
        return 0
    elif (O1 > O2):
        return 1
    else:
        return -1

def comparenationality(keynacionalidad,nacionalidad):
    """Name
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    nacionalentry = me.getKey(nacionalidad)
    if (keynacionalidad == nacionalentry):
        return 0
    elif (keynacionalidad > nacionalentry):
        return 1
    else:
        return -1
def comparemedio(keymedio,medio):
    """Name
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    medioentry = me.getKey(medio)
    if (keymedio == medioentry):
        return 0
    elif (keymedio > medioentry):
        return 1
    else:
        return -1

#comparacion requqrimiento 1(pruebaaa)
def comparefecha(keyfecha,fecha):
    """Name
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    fechaentry = me.getKey(fecha)
    if (keyfecha == fechaentry):
        return 0
    elif (keyfecha > fechaentry):
        return 1
    else:
        return -1

def cmpA_I(artist1, artist2):
    if artist1 < artist2:
        r = True
    else:
        r = False 
    return r
def cmpo(o1,o2):
    if o1 < o2:
        r = True
    else:
        r = False 
    return r


# Funciones de ordenamiento
def ordenamiento_Ndate(catalog):
    sorted_list = mrgs.sort(catalog, cmpfunction=cmpA_I)
    return sorted_list

#funcion de get

def getnationality(catalog):
    
    """
    Número de Nacionalidades en el catálogo
    """
    return mp.keySet(catalog['artistNationality'])

def getmedio(catalog):
    
    """
    Número de Nacionalidades en el catálogo
    """
    return mp.keySet(catalog['artworkmedium'])

def getfecha(catalog):
    
    """
    Número de Nacionalidades en el catálogo
    """
    return mp.keySet(catalog['BeginDate'])
