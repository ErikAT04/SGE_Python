"""
DICCIONARIOS: [HASHMAPS], guardan información en clave-valor
Es una estructura muy parecida a los objetos JSON
"""

 #Declaración
diccionario = {"Hola":"Adios",
                "24":"Hello",
                "Año": 2024
                }


#Acceso a objetos del diccionario
print(diccionario) #Imprime todo
print(diccionario["Año"]) #Si pones la clave te da el valor
#print(diccionario[2024]) #Esto no funciona
print(diccionario.get("Año")) #Funciona lo mismo
print(diccionario.keys()) #Imprime las claves del diccionario
print(diccionario.values()) #Imprime los valores del diccionario

diccionario["Año"] = 2025 #Cambia el valor

tupla = diccionario.items() #Devuelve los items del diccionario a modo de tupla
print(tupla)

boolean = ("Año" in diccionario) #Guarda si existe la CLAVE

diccionario.update({"Año" : 2024}) #Actualiza el valor de x clave

#Añadir contenido
diccionario["ASDF"] = "A" #Si metes una clave inexistente, la crea
diccionario.update({"Aa" : "Hi"}) #Igual con el update

#Bucles: muy parecido a las listas
for x in diccionario:
    print(x) #ForEach de las claves

for x in diccionario:
    print(diccionario[x]) #ForEach de valores

for x in diccionario.values():
    print(x) #ForEach de valores 2.0

for x in diccionario.keys():
    print(x) #ForEach de claves 2.0

for x, y in diccionario.items():
    print(f"Clave: {x} ; valor: {y}") #x es clave e y es valor



#Borrado de contenido
diccionario.pop("ASDF") #Borra la clave
diccionario.popitem() #Borra la última clave metida
del diccionario["24"] #Borra esa clave
del diccionario #Borra el diccionario