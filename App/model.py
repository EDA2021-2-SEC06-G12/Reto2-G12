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
                'artworkmedium': None,
                'artworks': None}

    catalog['artist'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')

    catalog['Medium'] = mp.newMap(815,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=compareMapMedium)

    catalog['Nationality'] = mp.newMap(840,
                                        maptype='PROBING',
                                        loadfactor=0.5,
                                        comparefunction=compareMapNationality)
    catalog["ObjectID"] = mp.newMap(840,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapObjectID)  
    catalog["ConstituentID"] = mp.newMap(837,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapConstituentID)                                 
    return catalog

# Funciones para agregar informacion al catalogo

def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mediums = artwork['Medium'].split(",")
    mp.put(catalog["ObjectID"], artwork["ObjectID"], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    mp.put(catalog["ConstituentID"],artist["ConstituentID"], artist)
    
# Funciones para creacion de datos


# Funciones de consulta
"""def total_obras_Nacionalidad(Nacionalidad,catalog):
    n_list=lt.newList
    n=mp.get(catalog['Nationality'])
    if Nacionalidad == n:
        for o in 
        lt.addLast(n_list,Nacionalidad)
    return lt.size(n_list)"""

# Funciones utilizadas para comparar elementos dentro de una lista
# Funciones de comparación 
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
def compareMapObjectID(O1, O2):
    if (O1 == O2):
        return 0
    elif (O1 > O2):
        return 1
    else:
        return -1
def compareMapConstituentID(C1, C2):
    if (C1 == C2):
        return 0
    elif (C1 > C2):
        return 1
    else:
        return -1
# Funciones de ordenamiento
