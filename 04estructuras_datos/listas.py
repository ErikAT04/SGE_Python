lista = ["Obj1", "Paco", 23, "Hola", "Genial", "Pedro"]
print(lista)
"""
Las listas son almacenes de objetos y valores. No es necesario declarar, pero por poder se puede escribir el valor seguido de []
Los índices de las listas empiezan en 0
"""
nuevaLista:int[12] #Declaración de una lista con valor fijo de tipo int

#Acceso al contenido de una lista:
print(lista[0]) #Se refiere al primer item
print(lista[-1]) #Se refiere al último item
print(lista[2:4]) #Muestra el rango entre 2 y 4 SIN INCLUIR EL 4
print(lista[:2]) #Muestra hasta la posición 2 (0, 1, 2)
print(lista[2:]) #Muestra desde la posición 2 hasta el final
boolean = ("Hola" in lista) #'' in list es una booleana que mira si un objeto está en la lista

#Cambio en listas:
lista[0] = "Obj2" #Sin más, cambiarlo
lista[1:3] = ["Merlina", "Jose"] #Cambias del rango 1 a 3 SIN INCLUIR EL 3

#Inserción de objetos
lista.insert(1, "AAAA") #Mueve todo una posición a la derecha para meter en el puesto 1 el objeto
lista.append(3.141592) #Inserta al final
lista.extend(nuevaLista) #Inserta una lista al final de la otra (en este caso nuevaLista al final de lista)

#Loop de listas
for x in lista:
    print(x) #ForEach

for i in range(len(lista)):
    print(lista[i]) #For con incremento que recorre la lista

i=0
while(i<len(lista)):
    print(lista[i])
    i+=1 #While que recorre la lista

[print(x) for x in lista] #Imprime con un for

#Orden de listas:
lista.sort() #Sort de la lista sin más
lista.sort(reverse=True) #Sort descendiente
lista.reverse #Sort al revés
"""REGLAS DEL SORT:
    1. Las mayúsculas van antes de las minúsculas
""" 

#Copia de listas:
lista2 = lista.copy() #Sin más
lista3 = lista.list(lista) #Otro tipo de copia
lista4 = lista[:] #Copia cada elemento de la lista

#Unión de listas:
lista5 = lista2+lista3 #"Suma" de listas
lista6 = [1, 2, 3]
for x in lista:
    lista6.append(x) #Va añadiendo al final cada elemento. 
lista7=[3, 5, 10]
lista7.extend(lista6) #Añade la lista 6 al final de la 7.

#Métodos de listas:
lista7.clear() #Borra los elementos de la lista
lista.count() #Muestra cuantos elementos tiene la lista
lista.index("Hola") #Muestra el índice del elemento en la lista.

#Eliminar objetos
lista.remove("Genial") #Borra a paco si lo encuentra. Si hay varias ocurrencias, borra la primera
lista.pop(0) #Borra según el índice
lista.pop() #Borra el último elemento
del lista[2] #Pop 2.0
del lista #Borra la lista