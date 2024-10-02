#TUPLAS: Guardan muchos objetos en una sola variable
tupla = ("Hola", "adios", 19, "asdf")
print(tupla)
"""
Las tuplas permiten que sean multi tipo o de un único tipo
Las tuplas permiten tener varios atributos del mismo valor
Las tuplas no permiten que cambien el valor de sus objetos una vez se crean, así como añadir objetos o borrarlos
"""
print(len(tupla)) #Saca la longitud de la tupla
tupla2 = ("a",) #Tupla de un solo objeto -> Sin la coma sería un objeto normal

tupla3 = tuple(("Hola", "Adios", "Perro")) #tuple es el Constructor

#Acceso a los datos:
print(tupla[0]) #Muestra el valor del indice 0 de la tupla
print(tupla[-1]) #Muestra el último valor
print(tupla[1:3]) #Muestra la tupla entre los índices 1 y 3 SIN INCLUIR EL 3
print(tupla[:2]) #Muestra del principio a la posición 2 de la tupla
print(tupla[1:]) #Muestra del valor 1 al final de la tupla
boolean = ("Hola" in tupla) #Guarda si existe el objeto en la tupla

#Cambiar valores en la tupla: Cambio de tupla a lista y de lista a tupla:
lista_tupla = list(tupla) #Convierto a lista
lista_tupla[0] = "aa"
tupla = tupla(lista_tupla) #Convierto a tupla

"""Esto es aplicable a TODAS LAS OPERACIONES DE LISTAS, puesto que la conviertes directamente a una lista"""

#Unión de tuplas:
tupla = tupla + tupla2 #Esto sí se permite por algún motivo

#Borrado de items en tuplas: Convierte de tupla a lista, hace cambio y de vuelta a tupla
lista_tupla = list(tupla) #Convierto a lista
lista_tupla.remove("aa")
tupla = tuple(lista_tupla) #Convierto a tupla

del tupla #Deja borrar la tupla sin más

#DESEMPAQUETAR TUPLAS: Dar valores a los items de una tupla
nuevaTupla = tuple(("Hola", "Buenas", "Adios"))
(prueba1, prueba2, prueba3) = nuevaTupla #Asigno el primer valor al indice 0, el segundo al indice 1 y así
print(f"{prueba1}, {prueba2}, {prueba3}")

(prueba1, *prueba2) = nuevaTupla #Si hay más valores en la tupla que en la toma de valores, se puede añadir un * para que el valor se convierta en una lista
(*prueba2, prueba3) = nuevaTupla #Ese asterisco se puede poner donde quiera, cabe recalcar

#Bucles: Igual que los bucles de listas
for x in nuevaTupla:
    print(x)

for i in range(len(nuevaTupla)):
    print(nuevaTupla[i])

i=0
while i<len(nuevaTupla):
    print(nuevaTupla[i])
    i+=1

#MULTIPLICACIÓN DE TUPLAS:
nuevaTupla = nuevaTupla*2 #Si, por algún motivo puedes hacer esto