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

from DISClib.Algorithms.Sorting import mergesort as mrgs
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mrgs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# INICIALIZACIÓN DE CATÁLOGO
# Catálogo Vacío
def newCatalog():

    catalog = {'artist': None,
                'artworks': None,
                'artistNationality': None,
                'id_artista': None,
                'BeginDate': None,
                'DateAcquired': None,
                'artista_obra': None,
                'artista_medio': None}
    
    catalog['artist'] = lt.newList('ARRAY_LIST', compareConstituentID)
    catalog['artworks'] = lt.newList('ARRAY_LIST', compareObjectID)

    '''
    Este indice crea un map cuya llave es el medio de una obra
    '''

    catalog['artistNationality'] = mp.newMap(2000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparenationality)
       
    catalog['id_artista'] = mp.newMap(2000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparemedio)                                    

    catalog['BeginDate']  = mp.newMap(2000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)

    catalog['DateAcquired'] = mp.newMap(2000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)

    catalog['artista_obra'] = mp.newMap(2000,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparemedio)  

    catalog['artista_medio'] = mp.newMap(2000,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparemedio)
    

    return catalog


# CARGA DE DATOS AL CATÁLOGO
# Carga de Artistas
def addArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    addid_artista(catalog, artist)
    addN_fecha(catalog, artist['BeginDate'], artist)

def addid_artista(catalog, artista):
    artistas = catalog['id_artista']
    exist = mp.contains(artistas, artista['ConstituentID'])
    if not exist:
        mp.put(artistas, artista['ConstituentID'], artista)

#Requerimiento 1
def addN_fecha(catalog, date, artista):
    fechas = catalog['BeginDate']
    exist = mp.contains(fechas, date)
    if not exist:
        artist = lt.newList('ARRAY_LIST')
        lt.addFirst(artist, artista)
        mp.put(fechas, date, artist)
    else:
        entry = mp.get(fechas, date)
        artist = me.getValue(entry)
        lt.addLast(artist, artista)

# Carga de Obras de Arte
def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    addDateAcquired(catalog, artwork['DateAcquired'], artwork)
    lista_ids = artwork['ConstituentID'].replace(" ","").replace("[","").replace("]","").split(",")
    for id_artist in lista_ids:
        entry = mp.get(catalog['id_artista'], id_artist)        
        artista = me.getValue(entry)
        addNationality(catalog, artista['Nationality'], artwork)
        addartist_artwork(catalog, artista['DisplayName'], artwork)

#Requerimiento 2
def addDateAcquired(catalog, dateacquired, artwork):
    fechas = catalog['DateAcquired']
    exist = mp.contains(fechas, dateacquired)
    if not exist:
        obra = lt.newList('ARRAY_LIST')
        lt.addFirst(obra, artwork)
        mp.put(fechas, dateacquired, obra)
    else:
        entry = mp.get(fechas, dateacquired)
        artist = me.getValue(entry)
        lt.addLast(artist, artwork)

#Requerimiento 3
def addartist_artwork(catalog, name, artwork):  #indice creado 
    o_catalog = catalog['artista_obra']
    exist_m = mp.contains(o_catalog, name)
    if exist_m:
        entry = mp.get(o_catalog, name)
        name1 = me.getValue(entry)   #entrando en el if 
    else:
        name1 = newname(name)
        mp.put(o_catalog, name, name1)
    if lt.isPresent(name1['artwork'], artwork) == 0:
        lt.addLast(name1['artwork'], artwork)
    lt.addLast(name1['artwork'], artwork)

def newname(name):
    
    name = {'name': "",
              "artwork": None,
              }
    name['name'] = name
    name['artwork'] = lt.newList('SINGLE_LINKED', compareObjectID)

    return name

#Requerimiento 4
def addNationality(catalog, nacionality, artwork):
    nacionalidades = catalog['artistNationality']
    exist = mp.contains(nacionalidades, nacionality)
    if not exist:
        obra = lt.newList('ARRAY_LIST')
        lt.addFirst(obra, artwork)
        mp.put(nacionalidades, nacionality, obra)
    else:
        entry = mp.get(nacionalidades, nacionality)
        obra = me.getValue(entry)
        lt.addLast(obra, artwork)
    '''n_catalog = catalog['artistNationality']
    exist_n = mp.contains(n_catalog, nacionality)
    if exist_n:
        entry = mp.get(n_catalog, nacionality)
        n_nacional = me.getValue(entry)   #entrando en el if 
    else:
        n_nacional = newnacionalidad(nacionality)
        mp.put(n_catalog, nacionality, n_nacional)
    if lt.isPresent(n_nacional['artwork'], artwork) == 0:
        lt.addLast(n_nacional['artwork'], artwork)'''

def newnacionalidad(nacionalidad):

    nationality = {'Nationality': "",
              "artwork": None,
              }

    nationality['Nationality'] = nacionalidad
    nationality['artwork'] = lt.newList('SINGLE_LINKED', compareObjectID)

    return nationality


# REQUERIMIENTO 1 (LISTAR CRONOLÓGICAMENTE LOS ARTISTAS)
def listar_artist_date(A_I, A_FN, catalog):
    artista = lt.newList('ARRAY_LIST')
    fechas_tot = catalog['BeginDate']
    fechas = mp.keySet(fechas_tot)
    orden = ordenamiento_artist_AI(fechas)
    for fecha in lt.iterator(orden):
        if (fecha >= A_I) and (fecha <= A_FN):
            entry = mp.get(fechas_tot, fecha)
            valor = me.getValue(entry)
            for artist in valor['elements']:
                lt.addLast(artista, artist)

    total = lt.size(artista)

    primeros = lt.subList(artista, 1, 3)
    ultimos = lt.subList(artista, lt.size(artista) - 2, 3)

    return total, primeros['elements'], ultimos['elements']

# REQUERIMIENTO 2 (LISTAR CRONOLÓGICAMENTE LAS ADQUISICIONES)
def listar_artwork_date(F_I, F_FN, catalog):
    obra = lt.newList('ARRAY_LIST')
    fechas_tot = catalog['DateAcquired']
    fechas = mp.keySet(fechas_tot)
    orden = ordenamiento_artist_AI(fechas)
    for fecha in lt.iterator(orden):
        if (fecha >= F_I) and (fecha <= F_FN):
            entry = mp.get(fechas_tot, fecha)
            valor = me.getValue(entry)
            for obr in valor['elements']:
                lt.addLast(obra, obr)

    total = lt.size(obra)

    primeros = lt.subList(obra, 1, 3)
    ultimos = lt.subList(obra, lt.size(obra) - 2, 3)

    return total, primeros['elements'], ultimos['elements']

# REQUERIMIENTO 3 (CLASIFICAR LAS OBRAS DE UN ARTISTA POR TÉCNICA)


# REQUERIMIENTO 4 (CLASIFICAR LAS OBRAS POR LA NACIONALIDAD DE SUS CREADORES)



# Funciones de consulta
#¿ELIMINAR?
def T_obras_nacionalidad (nacionalidad,catalog):
    
    nacionalidades = catalog['artistNationality']
    existnacionality = mp.contains(nacionalidades, nacionalidad)
    if existnacionality:
        entry = mp.get(nacionalidades, nacionalidad)
        entrynacionality = me.getValue(entry)
        totnacionalidad = lt.size(entrynacionality['artwork'])
        return totnacionalidad
    return 0

#///////////////////REQUERIMINTO 3///////////////////////////
#¿ELIMINAR?
def clasificacion_medio_t_obra(catalog,Name):
    c_artisto=catalog['artista_obra']
    existname= mp.contains(c_artisto, Name)
    if existname:
        entry = mp.get(c_artisto, Name)
        entryname = me.getValue(entry)
        totobras = lt.size(entryname['artwork'])
        sublist3_primeros= lt.subList(entryname['artwork'],1,3)
        sublist3_ultimos= lt.subList(entryname['artwork'],totobras-3,3)

        return (totobras,sublist3_primeros,sublist3_ultimos)

    return None

# Funciones utilizadas para comparar elementos dentro de una lista


#FUNCIONES DE COMPARACIÓN
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
    if (int(O1['ObjectID'])) == int(O2['ObjectID']):
        return 0
    elif (int(O1['ObjectID'])) > int(O2['ObjectID']):
        return 1
    else:
        return -1

def comparenationality(keynacionalidad,nacionalidad):
    """Name: comparenationality
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

#FUNCIONES DE ORDENAMIENTO
def ordenamiento_artist_AI(catalog):
    sorted_list = mrgs.sort(catalog, cmpfunction=cmpA_I)
    return sorted_list

#FUNCIONES ADICIONALES
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