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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

from time import process_time

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

csvcasting = "Data\AllMoviesCastingRaw.csv"
csvdetalles = "Data\AllMoviesDetailsCleaned.csv"
#csvcasting = "Reto2-202020-Template/Data/MoviesCastingRaw-small.csv"
#csvdetalles = "Reto2-202020-Template/Data/SmallMoviesDetailsCleaned.csv"
#csvcasting = "Reto2-202020-Template/Data/AllMoviesCastingRaw.csv"
#csvdetalles = "Reto2-202020-Template/Data/AllMoviesDetailsCleaned.csv"


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def muestrainfopeliculas (peliculaparametro, posicionpelicula):
    print ("La película en la posicion {}, corresponde a {}, se estrenó el {}, tiene una votación promedio de {} en un total de {} votos, y su idioma original es {}." .format (str (posicionpelicula), peliculaparametro['original_title'], peliculaparametro['release_date'], peliculaparametro['vote_average'], peliculaparametro['vote_count'], peliculaparametro['original_language']))

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    ejecuta = True
    while ejecuta:
        print("\n**Explorando la magia del cine recargado**")
        print ("Bienvenido, las siguientes son las opciones que puede consultar:\n")
        print("1- Cargar Datos")
        print("2- Cargar información en el catálogo")
        print("3- Descubrir productoras de cine") #req 1
        print("4- Conocer a un director") #req 2
        print("5- Conocer a un actor") #req 3
        print("6- Entender un género cinematográfico") #req 4
        print("7- Encontrar películas por país") #req 5
        print("0- Salir")

        inputs = input('\nSeleccione una opción para continuar\n')

        if int(inputs[0]) == 1:
            print ("cargando archivos...")
            tempcatalogostart = process_time() #inicia temporizador 
            catalog = controller.IniciarCatalogo()
            tempcatalogostop = process_time() #Termina temporizador
            print("\nCatálogo vacío creado, tiempo de carga: ",tempcatalogostop-tempcatalogostart," segundos")
            

        elif int(inputs[0]) == 2:
            tempcargastart = process_time()
            controller.cargardatos(catalog,csvdetalles,csvcasting)
            tempcargastop = process_time()
            print("\nSe cargaron en total {} datos al catálogo, tiempo de carga: {} segundos" .format(lt.size(catalog["pelis"]),tempcargastop-tempcargastart))
            #print (lt.size(catalog["pelis"]))

        elif int(inputs[0]) == 3:
            producername = input("Nombre de la productora de interes:\n")
            tempconsultstart = process_time() #inicia temporizador
            producerinfor = controller.getMoviesByProducer(catalog,producername)
            iterator = it.newIterator(producerinfor["movies"])  
            print ("\nLas películas que han sido creadas por {}, son:\n".format(producername))  
            indicepelicula = 0                 
            while  it.hasNext(iterator):
                element = it.next(iterator)
                indicepelicula += 1
                print(str(indicepelicula) + ".  " + element)
            print("\nEstas películas tuvieron un promedio de votación de: {}" .format(round(producerinfor["vote_average"], 3)))
            tempconsultstop = process_time() #termina temporizador
            print("\nEl tiempo que tardó esta consulta es de: {} segundos" .format(tempconsultstop-tempconsultstart))

        elif int(inputs[0]) == 4:
            DirectorName = input("Ingrese el nombre del director para el cual quiera conocer sus películas:\n")
            ValueDirector = controller.getMoviesByDirector(catalog,DirectorName)

            iterator=it.newIterator(ValueDirector["movies"])
            print("\n{} ha dirigido en total {} peliculas, estas son:\n" .format(DirectorName, (ValueDirector['movies']['size'])))
            sumatoria = 0
            while it.hasNext(iterator):
                element=it.next(iterator)
                movie=controller.getMovieByid(catalog,element)
                print("-> "+ movie["original_title"])
                sumatoria += float((movie["vote_average"]))

            print ("\nEstas películas tuvieron una votación promedio de {}." .format (str ( round ( (sumatoria/ValueDirector['movies']['size']) ,2))))

            pass
            #Aki Kaurismäki

        elif int(inputs[0]) == 5:
            actorname = input("Nombre del actor de interes:\n")
            actorinfor = controller.getMoviesByActor(catalog,actorname)
            iterator=it.newIterator(actorinfor["movies"])
            print("Las peliculas en las que ha actuado" + actorname + "son : ")
            suma= 0
            while it.hasNext(iterator):
                element=it.next(iterator)
                movie=controller.getMovieByid(catalog,element)
                print("->"+movie["original_title"])
                suma +=float((movie["vote_average"]))
            print("La cantidad de peliculas en las que ha actuado es "+str(lt.size(actorinfor["movies"])))
            print("El promedio de votacion de todas sus peliculas es "+str(round(suma/lt.size(actorinfor["movies"]),2)))
            print("El director con el que más ha participado es "+actorinfor["director"])
            pass
        elif int(inputs[0]) == 6:
            name = input("Nombre de el genero de interes\n")
            tempconsultstart = process_time() #inicia temporizador
            genreinfo = controller.getMoviesByGenre(catalog,name)
            iterator = it.newIterator(genreinfo["movies"])  
            print ("\nLas películas que pertenecen al genero {}, son:\n".format(name))  
            indicepelicula = 0                 
            while  it.hasNext(iterator):
                element = it.next(iterator)
                indicepelicula += 1
                print(str(indicepelicula) + ".  " + element)
            print("\nEstas películas tuvieron un promedio de votación de: {}" .format(round(genreinfo["vote_average"], 3)))
            tempconsultstop = process_time() #termina temporizador
            print("\nEl tiempo que tardó esta consulta es de: {} segundos" .format(tempconsultstop-tempconsultstart))      
        elif int(inputs[0]) == 0:
            ejecuta = False

printMenu()
