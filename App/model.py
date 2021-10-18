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
                'artworkmedium': None,
                'artistNationality': None}
    
    catalog['artist'] = lt.newList('ARRAY_LIST', compareConstituentID)
    catalog['artworks'] = lt.newList('ARRAY_LIST', compareObjectID)

    '''
    Este indice crea un map cuya llave es el medio de una obra
    '''

    catalog['artistNationality'] = mp.newMap(2000,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparenationality)
       
    catalog['id_artista'] = mp.newMap(2000,
                                        maptype='PROBING',
                                        loadfactor=2.0,
                                        comparefunction=comparemedio)                                    

    catalog['BeginDate']  = mp.newMap(2000,
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
    addid_artista(catalog,artist)
    addN_fecha(catalog,artist)

def addid_artista(catalog,artista):
    artistas= catalog["id_artista"]
    exist=mp.contains(artistas,artista['ConstituentID'])
    if not exist:
        mp.put(artistas,artista['ConstituentID'],artista)

#Requerimiento 1
def addN_fecha(catalog, artista):
    artistas= catalog["BeginDate"]
    exist=mp.contains(artistas,artista['BeginDate'])
    if not exist:
        mp.put(artistas,artista['BeginDate'],artista)

# Carga de Obras de Arte
def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    lista_ids= artwork['ConstituentID'].replace(" ","").replace("[","").replace("]","")
    for id_artist in lista_ids.split(","):
        entry=mp.get(catalog['id_artista'],id_artist)        
        artista=me.getValue(entry)
        addNationality(catalog,artista['Nationality'],artwork)
        addartist_artwork(catalog,artista['DisplayName'], artwork)

#Requerimiento 3
def addartist_artwork(catalog, name , artwork):  #indice creado 
    o_catalog= catalog['artista_obra']
    exist_m=mp.contains(o_catalog,name)
    if exist_m:
        entry=mp.get(o_catalog,name)
        name1=me.getValue(entry)   #entrando en el if 
    else:
        name1= newname(name)
        mp.put(o_catalog,name,name1)
    if lt.isPresent(name1['artwork'],artwork) == 0:
        lt.addLast(name1['artwork'],artwork)
    lt.addLast(name1['artwork'],artwork)

def newname(name):
    
    name = {'name': "",
              "artwork": None,
              }
    name['name'] = name
    name['artwork'] = lt.newList('SINGLE_LINKED', compareObjectID)

    return name

#Requerimiento 4
def addNationality(catalog, nacionality, artwork):
    n_catalog=catalog['artistNationality']
    exist_n=mp.contains(n_catalog,nacionality)
    if exist_n:
        entry=mp.get(n_catalog,nacionality)
        n_nacional=me.getValue(entry)   #entrando en el if 
    else:
        n_nacional= newnacionalidad(nacionality)
        mp.put(n_catalog,nacionality,n_nacional)
    if lt.isPresent(n_nacional['artwork'],artwork) == 0:
        lt.addLast(n_nacional['artwork'],artwork)

def newnacionalidad(nacionalidad):

    nationality = {'Nationality': "",
              "artwork": None,
              }

    nationality['Nationality'] = nacionalidad
    nationality['artwork'] = lt.newList('SINGLE_LINKED', compareObjectID)

    return nationality



# Funciones para creacion de datos

#///////////////////REQUERIMINTO 3///////////////////////////

#////////////////////////////////////////////////////////////
def newobra_artist(medio):
    
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
    
    nacionalidades = catalog['artistNationality']
    existnacionality = mp.contains(nacionalidades, nacionalidad)
    if existnacionality:
        entry = mp.get(nacionalidades, nacionalidad)
        entrynacionality = me.getValue(entry)
        totnacionalidad = lt.size(entrynacionality['artwork'])
        return totnacionalidad
    return 0
#///////////////////REQUERIMINTO 3///////////////////////////   
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
#///////////////////////////////////////////////////////////////    
#def sublista_tobras_artista():  

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





#comparacion requqrimiento 1(pruebaaa)


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

def getnationality(catalog, nacionalidad):
    
    """
    Número de Nacionalidades en el catálogo
    """
    n=nacionalidad
    return mp.get(catalog['artistNationality'],n)

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
