"""
En Python, una librería es un conjunto de módulos que contienen funciones, clases y variables para reutilizar
Las librerías python permiten aprovechar el código de otros desarrolladores que aceleran el desarrollo de programas.
    - Los módulos son archivos que contienen el código Python (.py)
    - Las librerías son un conjunto de esos módulos relacionados entre sí
Hay varios tipos de librerías:
    - Estándar: Vienen incluidas en Python (math, os, datetime, random...)
    - Externas: Van aparte y se tienen que importar en el workspace (NumPy, Panda, request...)
"""

#USO DE LIBRERÍAS
import math #Importa una librería interna
from math import sqrt #Importa un módulo de la librería
import numpy as np #Importa la librería con un nombre de variable
from numpy import * #Importa la librería entera, pero no es util porque puede dar problemas con conflictos o baja claridad en el código

#Importación de las externas: pip install (librería)