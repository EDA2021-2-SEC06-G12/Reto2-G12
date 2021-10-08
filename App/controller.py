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

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
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
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
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

def NationalitySize(catalog):
    """
    Número de Nacionalidades en el catálogo
    """
    return model.NationalitySize(catalog)

def MediumSize(catalog):
    """
    Número de Medios en el catálogo
    """
    return model.MediumSize(catalog)

def getnationality(catalog):

    return model.getnationality(catalog)

def getmedio(catalog):

    return model.getmedio(catalog)

