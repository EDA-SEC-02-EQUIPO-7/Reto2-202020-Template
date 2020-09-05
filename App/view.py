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

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

csvcasting = "Data/MoviesCastingRaw-small.csv"
csvdetalles = "Data/SmallMoviesDetailsCleaned.csv"



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
            
            casting = controller.llamarcargardatoslista(csvcasting)
            detalles = controller.llamarcargardatoslista(csvdetalles)
            print ("Se cargaron en total {} peliculas" .format(lt.size(detalles)))
            primerelemento = lt.firstElement(detalles)
            ultimoelemento = lt.lastElement(detalles)
            muestrainfopeliculas (primerelemento, 1)
            muestrainfopeliculas (ultimoelemento, lt.size(detalles))
            

        elif int(inputs[0]) == 2:
            pass

        elif int(inputs[0]) == 3:
            pass

        elif int(inputs[0]) == 4:
            pass

        elif int(inputs[0]) == 5:
            pass
        
        elif int(inputs[0]) == 0:
            ejecuta = False

printMenu()

