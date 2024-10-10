#JSON: Archivos de objetos en JavaScript que guardan e intercambian información con programas
#Usa atributos Clave:Valor (como en los diccionarios). Su estructura

import json #Es importante importar la librería json para poder abrirlo
import os

x = '{ "nombre":"Erik", "edad":19, "ciudad":"Valladolid"}' #Forma de JSON

y = json.loads(x) #Parsea el JSON

print(y) #Imprime el JSON entero

print(y["nombre"]) #Imprime solo el campo del nombre

#Convertir Python a JSON

x = { #Diccionaro en Python
    "nombre": "Erik",
    "edad": 19,
    "ciudad": "Valladolid"
}

y = json.dumps(x) #Convierte el diccionario a JSON

print(y) #Escribe el JSON

with open('Erik.json', 'w') as outfile: #Abre el archivo erik.json en modo escritura
    json.dump(x, outfile) #Mete en el archivo el json (outfile) el contenido de x como JSON


#El manejo de archivos json permite poder meter más de un dato en el diccionario o en el archivo
dictAlumnos = []
with open('alumnos.json', 'r') as infile: #Lee el json con más de un objeto
    dictAlumnos = json.load(infile) #Mete en el diccionario el contenido del json bien estructurado

print(dictAlumnos)

for x in dictAlumnos:
    print(x["Nombre"])


alumno = {
    "Nombre" : "Erik",
    "edad" : 19,
    "Fecha de nacimiento" : "04-01-2005",
    "Módulos" : ["Programación Multimedia y Dispositivos Móviles", "Sistemas de Gestión Empresarial", "Programación de Servicios y Procesos", "Acceso a Datos", "Empresa e Iniciativa Emprendedora", "Desarrollo de Interfaces"]
}

dictAlumnos = []

dictAlumnos.append(alumno)

alumno = {
    "Nombre" : "Angel",
    "edad" : 19,
    "Fecha de nacimiento" : "15-06-2005",
    "Módulos" : ["Programación Multimedia y Dispositivos Móviles", "Sistemas de Gestión Empresarial", "Programación de Servicios y Procesos", "Acceso a Datos", "Desarrollo de Interfaces"]
}

dictAlumnos.append(alumno)

with open('alumnos.json', 'w') as outfile:
    json.dump(dictAlumnos, outfile)

with open('alumnos.json', 'r') as infile:
    print(infile.read())

os.remove('alumnos.json') #Borra el archivo