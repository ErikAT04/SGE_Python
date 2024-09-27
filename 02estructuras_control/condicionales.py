#ESTRUCTURA IF -> Condicional de booleana simple (si/si no)
num:int = int(input("Escribe un número: "))
num2:int = int(input("Escribe otro número: "))
if(num>num2):
    print("El primer número es mayor que el seugundo") #Si el primero es mayor que el segundo, dice esto
else:
    print("El primer número no es mayor que el segundo") #Si no, dice esto

#Otra forma de usar if-else es con un Operador Ternario:
print("El primer número " + ("no ","")[num>num2] + "es mayor que el segundo") #Explicación: (casoFalso,casoVerdadero)[condición]


#ESTRUCTURA WHEN -> Condicional de múltiples casos (caso 1, caso 2, caso 3, caso por defecto...)
num = int(input("Escribe un número del 1 al 3: "))
match(num):
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _: #En el caso de que no se cumpla ningún otro caso:
        print("No válido")