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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
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
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapMedium)
    
    '''
    Este indice crea un map cuya llave es la nacionalidad de un artista
    '''

    catalog['artistNationality'] = mp.newMap(840,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapNationality)
                                     
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    addMediums(catalog)

def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    addNationality(catalog)

def addMediums(catalog):
    for obra in catalog['artworks']['elements']:
        medio = obra['Medium']
        ConsID = obra['ConstituentID']
        mp.put(catalog['artworkmedium'], medio, ConsID)


def addNationality(catalog):
    for artista in catalog['artist']['elements']:
        nacionalidad =  artista['Nationality']
        ConsID =  artista['ConstituentID']
        mp.put(catalog['artistNationality'], nacionalidad, ConsID)
    
# Funciones para creacion de datos


# Funciones de consulta

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

def compareMapMedium(medium1, medium2):
    if (medium1 == medium2):
        return 0
    elif (medium1 > medium2):
        return 1
    else:
        return -1

def compareMapNationality(N1, N2):
    if (N1 == N2):
        return 0
    elif (N1 > N2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
