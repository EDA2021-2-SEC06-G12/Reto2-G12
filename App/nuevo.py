# Función línea 41 Model.py
'''catalog["ObjectID"] = mp.newMap(840,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapObjectID)  
    catalog["artConstituentID"] = mp.newMap(837,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareMapConstituentID)'''

# Agregar Información al Catálogo

'''def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['artConstituentID'], artwork["ConstituentID"], artwork)
    mediums = artwork['Medium'].split(",")
    for medium in mediums:
        addartMedium(catalog, medium.strip(), artwork)

def addartMedium(catalog, mediumname, artwork):
    mediums = catalog['artworkmedium']
    existmed = mp.contains(mediums, mediumname)
    if existmed:
        entry = mp.get(mediums, mediumname)
        medium = me.getValue(entry)
    lt.addLast(medium['artworks'], artwork)


def addArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    mp.put(catalog['artistNationality'], artist["ConstituentID"], artist)
    artists = artist['Nationality'].split(",")
    for artist in artists:
        addArtistNat(catalog, artist.strip(), artist)

def addArtistNat(catalog, artistname, artist):
    artists = catalog['artistNationality']
    existart = mp.contains(artists, artistname)
    if existart:
        entry = mp.get(artists, artistname)
        medium = me.getValue(entry)
    lt.addLast(medium['artist'], artist)'''

# Funciones Comparación

'''def compareMapObjectID(O1, O2):
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
        return -1'''

# Funciones consulta

'''def total_obras_Nacionalidad(Nacionalidad,catalog):
    n_list=lt.newList
    n=mp.get(catalog['Nationality'])
    if Nacionalidad == n:
        for o in 
        lt.addLast(n_list,Nacionalidad)
    return lt.size(n_list)'''



    #FUNCIONES DE PRUEBA -DANIELA 

    ##########################################################

#FUNCION DE AGREGAR INFO AL CATALOGO (PRUEBAA)
"""
def addnacionalidadobras(catalog, nacionalidad, artwork):
    ""
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.

    nacionalidad = input 
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    ""
    nacionalidades = catalog['artistNationality'] 
    existnacionalidad = mp.contains(artwork, nacionalidades)
    if existnacionalidad:
        entry = mp.get(nacionalidades, artwork)
        nacionalidad = me.getValue(entry)
    else:
        nacionalidad = newnacionalidad(nacionalidad)
        mp.put(nacionalidades, nacionalidad, artwork)
    lt.addLast(nacionalidad['artwork'], artwork)

def addmedios(catalog, medio, artwork):
    ""
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.

    nacionalidad = input 
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    ""
    medios = catalog['artistNationality'] 
    existmedios = mp.contains(artwork, medios)
    if existmedios:
        entry = mp.get(medios, artwork)
        medio = me.getValue(entry)
    else:
        medio = newmedio(medios)
        mp.put(medios, medio, artwork)
    lt.addLast(medio['artwork'], artwork) 


lista de obras por una nacionalidad 
    for obra in catalog['artworks']['elements']:
            ConsOID= obra['ConstituentID']
            OBJID= obra['ObjectID']
            for CID in ConsOID:
                if CID == ConsID:
                    lt.addLast(lst_obras,OBJID)

"""
#####################################################
