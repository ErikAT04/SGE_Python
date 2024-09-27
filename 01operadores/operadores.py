print(f"Suma: 8 + 14 = {8+14}") #El corchete en este print con formato (print(f"texto")) permite realizar operaciones y funciones dentro de una cadena de caracteres

#Para obtener el texto de la consola de comandos, se utiliza el comando input(), donde se puede añadir dentro del paréntesis una frase que diga el programa a lo "Introduce un número"
try:
    numero:int = int(input("Escribe un número: "))
    print(f"Tu número es {numero}")
except:
    print("Eso no era un número")

numero = int(input())