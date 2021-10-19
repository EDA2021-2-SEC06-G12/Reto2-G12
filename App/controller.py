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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# INICIALIZACIÓN DE CATÁLOGO
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# CARGA DE DATOS AL CATÁLOGO
def loadData (catalog):
    loadArtists (catalog)
    loadArtworks (catalog)

def loadArtists (catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile,encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks (catalog):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile,encoding='utf-8'))
    for artworks in input_file:
        model.addArtworks(catalog, artworks)

def artistSize(catalog):
    """
    Numero de artistas cargados al catalogo 
    """
    return model.artistSize(catalog)

def artworkSize(catalog):
    """
    Numero de Obras de Arte cargados al catalogo
    """
    return model.artworkSize(catalog)

# REQUERIMIENTO 1 (LISTAR CRONOLÓGICAMENTE LOS ARTISTAS)
def listar_artist_date(A_I, A_FN, cont):
    Algoritmo = model.listar_artist_date (A_I, A_FN, cont)
    return Algoritmo

# REQUERIMIENTO 2 (LISTAR CRONOLÓGICAMENTE LAS ADQUISICIONES)
def listar_artwork_date(F_I, F_FN, cont):
    Algoritmo = model.listar_artwork_date(F_I, F_FN, cont)
    return Algoritmo

# REQUERIMIENTO 3 (CLASIFICAR LAS OBRAS DE UN ARTISTA POR TÉCNICA)
def clasificacion_medio_t_obra(Name, cont):
    Algoritmo = model.clasificacion_medio_t_obra(Name, cont)
    return Algoritmo

# REQUERIMIENTO 4 (CLASIFICAR LAS OBRAS POR LA NACIONALIDAD DE SUS CREADORES)
def Obras_Nacionalidad(cont):
    Algoritmo = model.Obras_Nacionalidad(cont)
    return Algoritmo

# REQUERIMIENTO 5 (TRANSPORTAR OBRAS DE UN DEPARTAMENTO)
def Costo_departamento(department, cont):
    Algoritmo = model.Costo_departamento(department, cont)
    return Algoritmo