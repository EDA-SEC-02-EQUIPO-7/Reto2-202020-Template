"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

import csv

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

def newmovie():
    lista=lt.newList('SINGLE_LINKED')

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def addmovielst(lst,movie):
    lt.addLast(lst,movie)

# Funciones para agregar informacion al catalogo



# -----------------------------------------------------
# -----------------------------------------------------
# Catálogo vacío
# Catálogo vacío
# Catálogo vacío
# -----------------------------------------------------
# -----------------------------------------------------

#'CHAINING'
#"PROBING"

def newCatalog():
    """ Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas

    Se crean indices (Maps) por los siguientes criterios:
    Productoras
    Directores
    Actores
    Géneros
    Pais

    Retorna el catalogo inicializado.
    """
    catalog = {'pelis': None,
               'MoviesIds': None,
               'Producers': None,
               'Directors': None,
               'Actors': None,
               'Genres': None,
               'Country': None}

    catalog['pelis'] = lt.newList('SINGLE_LINKED', CompareMoviesIds)

    catalog['MoviesIds'] = mp.newMap(500000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)

    catalog['Producers'] = mp.newMap(500000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=CompareProducersByName)

    catalog['Directors'] = mp.newMap(500000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=CompareDirectorsByName)

    catalog['Actors'] = mp.newMap(500000,
                                  maptype='PROBING',
                                  loadfactor=0.5,
                                  comparefunction=CompareActorsByName)
    catalog['Genres'] = mp.newMap(500000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=CompareGenresByName)

    catalog['Country'] = mp.newMap(500000,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=CompareCountriesByName)

    return catalog


# -----------------------------------------------------
# -----------------------------------------------------
# Catálogo vacío
# Catálogo vacío
# Catálogo vacío
# -----------------------------------------------------
# -----------------------------------------------------
def newProducer (producername):
    producer = {'name': None , "movies": None,  "vote_average": 0}
    producer['name'] = producername
    producer['movies'] = lt.newList("ARRAY_LIST",CompareMoviesIds)
    return producer

def newActor(actorname):
    actor = {'name': None , "movies": None,  "vote_average": 0}
    actor['name'] = actorname
    actor['movies'] = lt.newList("ARRAY_LIST",CompareMoviesIds)
    actor["direc"]=mp.newMap(7,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=CompareDirectorsByName)
    actor["mayor"]=0
    actor["director"]=""
    return actor



def newDirector (DirectorName):
    EachDirector = {'name': None , "movies": None}
    EachDirector['name'] = DirectorName
    EachDirector['movies'] = lt.newList("ARRAY_LIST",CompareMoviesIds)
    return EachDirector


#================================
#Funiones para agregar informacion
#Funiones para agregar informacion 
#Funiones para agregar informacion  
#================================

def addmovie (catalog,movie):
    # Agrega una pelicula a la lista de peliculas (pelis) y en el catalogo (MoviesIds)
    lt.addLast(catalog["pelis"],movie)
    mp.put(catalog["MoviesIds"],movie["id"],movie)
    "Funciones Adicionales de agregar"

def addMovieProducer(catalog, producername, movie):
    producers = catalog["Producers"]
    existproducer = mp.contains(catalog["Producers"],producername)
    if existproducer:
        entry = mp.get(producers,producername)
        producer = me.getValue(entry)
    else:
        producer = newProducer(producername)
        mp.put(producers, producername, producer)
    lt.addLast(producer["movies"], movie["original_title"])

    producer_average = producer["vote_average"]
    movie_average = movie["vote_average"]
    if ( producer_average == 0.0):
        producer["vote_average"] = float(movie_average)
    else:
        producer["vote_average"] = (producer_average  + float(movie_average)) / 2

def addMovieActor(catalog,actorname,movie):
    actors= catalog["Actors"]
    exist=mp.contains(catalog["Actors"],actorname)
    if exist:
        entry=mp.get(actors,actorname)
        actor=me.getValue(entry)
    else:
        actor=newActor(actorname)
        mp.put(actors,actorname,actor)
    lt.addLast(actor["movies"],movie["id"])
    exi=mp.contains(actor["direc"],movie["director_name"])
    if exi:
        entry=mp.get(actor["direc"],movie["director_name"])
        part=me.getValue(entry)
        mp.put(actor["direc"],movie["director_name"],part+1)
    else:
        mp.put(actor["direc"],movie["director_name"],1)
    entry=mp.get(actor["direc"],movie["director_name"])
    par=me.getValue(entry)
    if par>actor["mayor"]:
        actor["mayor"]=par
        actor["director"]=me.getKey(entry)



def addMovieDirector(catalog, DirectorName, movie):

    MapDirectorsInCatalog = catalog["Directors"]
    ExistDirector = mp.contains(MapDirectorsInCatalog,DirectorName)

    if ExistDirector:
        entry = mp.get(MapDirectorsInCatalog,DirectorName)
        MovieDirector = me.getValue(entry)

    else:
        MovieDirector = newDirector(DirectorName)
        mp.put(MapDirectorsInCatalog, DirectorName, MovieDirector)

    lt.addLast(MovieDirector["movies"], movie["id"])
    




# ==============================
# Funciones de consulta
# ==============================

def getmovie(lst,pos):
    element=lt.getElement(lst,pos)
    return element

def getMoviesByProducer(catalog,autorname): #Obtiene las peliculas de una productora
    producer = mp.get(catalog["Producers"],autorname)
    if producer:
        return me.getValue(producer)
    return None

def getMoviesByActor(catalog,actorname): #Obtiene las peliculas de una productora
    actor = mp.get(catalog["Actors"],actorname)
    if actor:
        return me.getValue(actor)
    return None





def getMoviesByDirector(catalog,DirectorName): #Obtiene las peliculas de una productora
    aDirector = mp.get(catalog["Directors"],DirectorName)
    if aDirector:
        return me.getValue(aDirector)
    return None





def getMoviesByid(catalog,id):
    title=mp.get(catalog['MoviesIds'],id)
    if title:
        return me.getValue(title)
    return None

# ==============================
# Funciones de Comparacion
# ==============================

def CompareMoviesIds(id1, id2):
    """
    Compara dos ids de peliculas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > (int(identry))):
        return 1
    else:
        return -1

def CompareProducersByName(keyname, producer):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    prodentry = me.getKey(producer)
    if (keyname == prodentry):
        return 0
    elif (keyname > prodentry):
        return 1
    else:
        return -1


def CompareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    direntry = me.getKey(director)
    if (keyname == direntry):
        return 0
    elif (keyname > direntry):
        return 1
    else:
        return -1



def CompareActorsByName(keyname, actor):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    acentry = me.getKey(actor)
    if (keyname == acentry):
        return 0
    elif (keyname > acentry):
        return 1
    else:
        return -1



def CompareGenresByName(keyname, genre):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    genentry = me.getKey(genre)
    if (keyname == genentry):
        return 0
    elif (keyname > genentry):
        return 1
    else:
        return -1


def CompareCountriesByName(keyname, country):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    counentry = me.getKey(country)
    if (keyname == counentry):
        return 0
    elif (keyname > counentry):
        return 1
    else:
        return -1
