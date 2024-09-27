# BUCLE FOR: Bucle que sigue patrones
#Hay varios tipos de for

#1. FOR DE RANGO X..Y
for i in range(1, 9):
    print(i) #Imprime todos los numeros de 1 a 9

#2. FOR DE CONJUNTOS
strings = ["Hola", "Adios", "Buenas"]
for i in strings:
    print(i) #Imprime Hola, luego Adios, luego Buenas

#3. FOR DE STRINGS
for i in "Hola":
    print(i) #Imprime primero H, luego o, luego l, y luego a

# BUCLE WHILE: Bucle con condicional
letra = input("Escribe 'a': ")
while(letra != "a"): #Mientras que la letra que se ponga no sea "a", se repetirá lo siguiente:
    letra = input("Que escribas 'a': ")

#EJEMPLOS DE BUCLES: TABLAS DE MULTIPLICAR
num:int = 8
#For de rango:
for i in range(1, 11): # de 1 a 10, en 11 se sale
    print(f"{num} * {i} = {num*i}")

#For de conjuntos
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f"{num} * {i} = {num*i}")

#~For de strings
for i in "123456789":
    print(f"{num} * {int(i)} = {num*int(i)}")

#while
iterador:int = 1
while (iterador<=10):
    print(f"{num} * {iterador} = {num*iterador}")
    iterador+=1