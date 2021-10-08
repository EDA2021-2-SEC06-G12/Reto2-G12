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