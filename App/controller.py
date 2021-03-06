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

import config as cf
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  TADlista datos
# ___________________________________________________
def cargardatos (catalog,moviesfile,file2):
    loadMovies(catalog,moviesfile,file2)

def loadMovies (catalog,file,file2, sep=";"):
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding='utf-8-sig') as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                model.addmovie(catalog,row)
                producername = row["production_companies"]
                model.addMovieProducer(catalog,producername,row)
                genres = row["genres"]
                genres = genres.replace("|"," ")
                genres = genres.split()

                for i in genres:
                    model.addMovieGenre(catalog,i,row)
                EachCountry = row["production_countries"]
                model.addMovieCountry(catalog,EachCountry,row)
    except:
        print("Hubo un error con la carga del archivo")
    try:
        with open(file2,encoding='utf-8-sig') as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                actor1=row["actor1_name"]
                actor2=row["actor2_name"]
                actor3=row["actor3_name"]
                actor4=row["actor4_name"]
                actor5=row["actor5_name"]
                model.addMovieActor(catalog,actor1,row)
                model.addMovieActor(catalog,actor2,row)
                model.addMovieActor(catalog,actor3,row)
                model.addMovieActor(catalog,actor4,row)
                model.addMovieActor(catalog,actor5,row)
                DirectorName = row["director_name"]               
                model.addMovieDirector(catalog,DirectorName,row)
                model.addCasting(catalog,row)
    except:
        print("Hubo un error con la carga del archivo")
    




def cargardatosmovies (file, sep=";"):
    lst = model.newlistmovie()#Usando implementacion arraylist
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding='utf-8-sig') as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                model.addmovielst(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
        
    


# ___________________________________________________
#  TAD map datos
# __________________________________________________


def lastmovie(lst):
    movie=model.getmovie(lst,lst["size"])
    return movie

def firstmovie(lst):
    movie=model.getmovie(lst,1)
    return movie

# ___________________________________________________
#  Catálogo
# ___________________________________________________


def IniciarCatalogo():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


#Se cargan las peliculas desde el csv al catálogo

# Funciones Requeromientos 

def getMoviesByProducer(catalog,producername):
    producerinfo = model.getMoviesByProducer(catalog,producername)
    return producerinfo

def getMoviesByActor(catalog,actorname):
    info=model.getMoviesByActor(catalog,actorname)
    return info

def getMoviesByDirector(catalog,DirectorName):
    info=model.getMoviesByDirector(catalog,DirectorName)
    return info

def getMoviesByGenre (catalog,genrename):
    genreinfo = model.getMoviesByGenre(catalog,genrename)
    return genreinfo

def getMoviesByCountry (catalog,CountryName):
    InfoPerCountry = model.getMoviesByCountry(catalog,CountryName)
    return InfoPerCountry

def getMovieByid(catalog,id):
    movie=model.getMoviesByid(catalog,id)
    return movie
def getMovieByid2(catalog,id):
    movie=model.getMoviesByid2(catalog,id)
    return movie


