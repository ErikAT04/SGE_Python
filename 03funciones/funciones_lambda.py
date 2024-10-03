"""
Las funciones Lambda son funciones anónimas hechas para ser guardadas en valores de tipo función
Pueden coger cualquier tipo de valor y tantos como quieran, pero solo pueden devolver un único valor
"""

#DECLARACIÓN -> Función = lambda [argumentos] : [devolución]
x = lambda : "Hola Mundo" #Función que devuelve el string "Hola Mundo"
print(x()) #Llama a la función

y = lambda a, b, c : a + b + c #Función que devuelve la suma de 3 parámetros que se le pasa
print(y(1, 2, 3))

#Función que devuelve una lambda ("Recursión")
def funcion(n):
    return lambda a : a + n #Lambda coge n de la función y la suma a otro valor recibido por paréntesis

print(funcion(2)(11)) #El primer paréntesis es n, y el segundo es a

z = funcion(3) #Guarda la llamada de la función (en este caso está guardando lambda(a) con el valor n = 3)

print(z(0))
print(z(4))

"""Su uso se ve en funciones de orden superior (map(), filter(), reduce()...) (las funciones que tienen como parámetro otra función)"""

