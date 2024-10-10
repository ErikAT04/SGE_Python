import json
import os


class Alumno:
    nombre:str
    edad:int
    fecha_nacimiento:str
    modulos:list[str]

    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos

    def __str__(self) ->str:
        return f"{self.nombre} {str(self.edad)} {str(self.fecha_nacimiento)} {str(self.modulos)}"

alumno = {
    "Nombre" : "Erik",
    "edad" : 19,
    "Fecha de nacimiento" : "04-01-2005",
    "Modulos" : ["Programación Multimedia y Dispositivos Móviles", "Sistemas de Gestión Empresarial", "Programación de Servicios y Procesos", "Acceso a Datos", "Empresa e Iniciativa Emprendedora", "Desarrollo de Interfaces"]
}

with open("alumnos.json", "w") as f:
    json.dump(alumno, f)

with open("alumnos.json", "r") as f:
    alumJSON = json.load(f)

alumnoObj:Alumno = Alumno(alumJSON["Nombre"], alumJSON["edad"], alumJSON["Fecha de nacimiento"], alumJSON["Modulos"])

print(alumnoObj)

os.remove("alumnos.json")