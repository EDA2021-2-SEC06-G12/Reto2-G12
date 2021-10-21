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
                'artista_obra': None}
    
    catalog['artist'] = lt.newList('ARRAY_LIST', compareConstituentID)
    catalog['artworks'] = lt.newList('ARRAY_LIST', compareObjectID)

    '''
    Este indice crea un map cuya llave es el medio de una obra
    '''

    catalog['artistNationality'] = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparenationality)
       
    catalog['id_artista'] = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparemedio)                                    

    catalog['BeginDate']  = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)

    catalog['DateAcquired'] = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)
    
    catalog['Department'] = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=comparefecha)

    catalog['artista_obra'] = mp.newMap(20000,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
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
    addDepartment(catalog, artwork['Department'], artwork)
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
def addartist_artwork(catalog, name, artwork):
    artistas = catalog['artista_obra']
    exist = mp.contains(artistas, name)
    if not exist:
        obra = lt.newList('ARRAY_LIST')
        lt.addFirst(obra, artwork)
        mp.put(artistas, name, obra)
    else:
        entry = mp.get(artistas, name)
        obra = me.getValue(entry)
        lt.addLast(obra, artwork)

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

#Requerimiento 5
def addDepartment(catalog, department, artwork):
    departamentos = catalog['Department']
    exist = mp.contains(departamentos, department)
    if not exist:
        obra = lt.newList('ARRAY_LIST')
        lt.addFirst(obra, artwork)
        mp.put(departamentos, department, obra)
    else:
        entry = mp.get(departamentos, department)
        artist = me.getValue(entry)
        lt.addLast(artist, artwork)

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

    return total, primeros['elements'], ultimos['elements'], artista

# REQUERIMIENTO 2 (LISTAR CRONOLÓGICAMENTE LAS ADQUISICIONES)
def listar_artwork_date(F_I, F_FN, catalog):
    contador = 0
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

    for obr in lt.iterator(obra):
        if 'Purchase' in obr['CreditLine'] or 'purchase' in obr['CreditLine']:
            contador += 1

    return total, primeros['elements'], ultimos['elements'], contador

# REQUERIMIENTO 3 (CLASIFICAR LAS OBRAS DE UN ARTISTA POR TÉCNICA)
def clasificacion_medio_t_obra(Name, catalog):
    todos = lt.newList('ARRAY_LIST')
    medios = lt.newList('ARRAY_LIST')
    artistas = catalog['artista_obra']
    artista = mp.get(artistas, Name)
    obras_artista = me.getValue(artista)
    for obras in lt.iterator(obras_artista):
        medio = obras['Medium']
        tec_incluida= False
        for obra_i in lt.iterator(medios):
            if medio == obra_i:
                tec_incluida = True
        if not tec_incluida:
            lt.addLast(medios, medio)

    contador_mayor = 0
    tecnica_mayor = ""
    for obra_medio in lt.iterator(medios):
        contador = 0
        for obras in lt.iterator(obras_artista):
            medio = obras['Medium']
            if obra_medio == medio:               
                contador += 1
        if contador > contador_mayor:
            contador_mayor = contador
            tecnica_mayor = obra_medio
        tupla = obra_medio, contador
        lt.addLast(todos,tupla)
    t_medio=lt.size(todos)
    t_obras = lt.size(obras_artista)
    lst_tecnicamayor= lt.newList('ARRAY_LIST')
    for obras in lt.iterator(obras_artista):
        medio = obras['Medium']
        if tecnica_mayor == medio:
            lt.addLast(lst_tecnicamayor, obras)
    primeros_3 = lt.subList(lst_tecnicamayor, 1, 3)
    ultimas = lt.subList(lst_tecnicamayor, lt.size(lst_tecnicamayor) - 2, 3)

    return t_obras, t_medio, tecnica_mayor, lst_tecnicamayor, primeros_3['elements'], ultimas['elements']

# REQUERIMIENTO 4 (CLASIFICAR LAS OBRAS POR LA NACIONALIDAD DE SUS CREADORES)
def Obras_Nacionalidad(catalog):
    cuantos = 0
    valores = lt.newList('ARRAY_LIST')
    nacionalidades = catalog['artistNationality']
    cada_una = mp.keySet(nacionalidades)
    for nacionalidad in lt.iterator(cada_una):
        if nacionalidad == '' or nacionalidad == 'Nationality unknown':
            entry = mp.get(nacionalidades, nacionalidad)
            valor = me.getValue(entry)['size']
            cuantos += valor
            dic = (cuantos, 'Nationality unknown')
        else:
            entry = mp.get(nacionalidades, nacionalidad)
            valor = me.getValue(entry)['size']
            dic = (valor, nacionalidad)

        lt.addLast(valores, dic)

    orden = ordenamiento(valores)
    mayores = lt.subList(orden, 1, 10)

    primeros = mp.get(nacionalidades, lt.getElement(mayores, 1)[1])
    primeros_3 = lt.subList(me.getValue(primeros), 1, 3)
    ultimas = lt.subList(me.getValue(primeros), lt.size(me.getValue(primeros)) - 2, 3)

    return mayores['elements'], primeros_3['elements'], ultimas['elements']

# REQUERIMIENTO 5 (TRANSPORTAR OBRAS DE UN DEPARTAMENTO)
def Costo_departamento(department, catalog):
    costo = 0
    mayor = 0
    lst_fechas_o = lt.newList('ARRAY_LIST')
    lst_costo_i = lt.newList('ARRAY_LIST')
    departamentos = catalog['Department']
    departamento = mp.get(departamentos, department)
    obras = me.getValue(departamento)
    total_obras = lt.size(obras)
    for obra in lt.iterator(obras):
        costo_i = 0
        depth = obra['Depth (cm)']
        diameter = obra['Diameter (cm)']
        height = obra['Height (cm)']
        length = obra['Length (cm)']
        width = obra['Width (cm)']
        date = obra['Date']
        if date != '':
            tupla_date = date, obra
            lt.addLast(lst_fechas_o, tupla_date)
            
        x = Dimensiones(depth, diameter, height, length, width)
        if x == -1:
            costo += 48 
            costo_i = 48 
        else:
            costo_1 = x * 72
            costo += costo_1
            costo_i = x * 72
        tupla = costo_i, obra
        lt.addLast(lst_costo_i, tupla)

    costo_total = round(costo, 3)

    orden_1 = ordenamientos(lst_costo_i)
    orden_2 = ordenamientos(lst_fechas_o)

    primeros = lt.subList(orden_2, 1, 5)
    ultimos = lt.subList(orden_1, lt.size(orden_1) - 4, 5)

    lista_f = Valores(primeros, ultimos)
    
    return total_obras, costo_total, lista_f[0]['elements'], lista_f[1]['elements']

def Valores(primeros, ultimos):
    primeros_5 = lt.newList('ARRAY_LIST')
    ultimos_5 = lt.newList('ARRAY_LIST')
    for valor in lt.iterator(primeros):
        obra = valor[1]
        lt.addLast(primeros_5, obra)
    for value in lt.iterator(ultimos):
        obras = value[1]
        lt.addLast(ultimos_5, obras)
    
    return primeros_5, ultimos_5


def Dimensiones(depth, diameter, height, length, width):
    contador = 0
    no_hay = True
    dimensiones = -1
    posicion = 1

    medidas = lt.newList("ARRAY_LIST")
    lt.addLast(medidas, depth)
    lt.addLast(medidas, height)
    lt.addLast(medidas, length)
    lt.addLast(medidas, width)
    lt.addLast(medidas, diameter)

    while posicion <= lt.size(medidas):
        dimension = lt.getElement(medidas, posicion)
        if (dimension != '') and (dimension != '0'):
            lt.changeInfo(medidas, posicion, float(dimension))
            contador += 1
            no_hay = False
        else:
            lt.changeInfo(medidas, posicion, 1)
        posicion += 1

    factor = 10**(-2*contador)

    if no_hay == False:
        if diameter != '':
            diameter = lt.getElement(medidas, 5)
            height = lt.getElement(medidas, 2)
            dimensiones = 3.1416 * ((diameter/2)**2) * height * factor/100
        
        else:
            depth = lt.getElement(medidas, 1)
            height = lt.getElement(medidas, 2)
            length = lt.getElement(medidas, 3)
            width = lt.getElement(medidas, 4)
            dimensiones =  depth * height * length * width * factor

    return dimensiones

# REQUERIMIENTO 6 (ENCONTRAR LOS ARTISTAS MÁS PROLÍFICOS)
def Artista_prolifico(cronologia, num_artistas, catalog):
    num_obras = lt.newList('ARRAY_LIST')
    obras_artista = catalog['artista_obra']
    for artista in cronologia:
        nombre = artista['DisplayName']
        entry = mp.get(obras_artista, nombre)
        valor = me.getValue(entry)
        tupla = valor, nombre
        lt.addFirst(num_obras, tupla)
    
    orden = ordenamiento(num_obras)
    return orden


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

def cmpA_IN(artist1, artist2):
    if artist1 > artist2:
        r = True
    else:
        r = False 
    return r

def cmpA(artist1, artist2):
    if artist1[0] < artist2[0]:
        r = True
    else:
        r = False 
    return r

#FUNCIONES DE ORDENAMIENTO
def ordenamiento_artist_AI(catalog):
    sorted_list = mrgs.sort(catalog, cmpfunction=cmpA_I)
    return sorted_list

def ordenamiento(catalog):
    sorted_list = mrgs.sort(catalog, cmpfunction=cmpA_IN)
    return sorted_list

def ordenamientos(catalog):
    sorted_list = mrgs.sort(catalog, cmpfunction=cmpA)
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