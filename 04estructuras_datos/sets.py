"""
SETS: ESTRUCTURAS DESORDENADAS QUE GUARDAN MUCHOS DATOS
No permiten buscar datos como tal y se trabaja a modo de hash.
No puedes tener elementos repetidos
"""

set = {"Perro", "Hola", 123}

#Adición:
set.add("Adios")

#Eliminado:
set.remove("Perro")

#No puede actualizar un valor, ya que no hay forma de acceder a los datos
#Si quieres actualizar un dato, eliminas y añades.

#Unión de sets:
set2 = {123, 22, 11}
set.union(set2) #Une sets. Permite meter unos cuantos.