"""
2º DAM, Sistemas de Gestión Empresarial
Erik Amo Toquero, curso 2024-25
"""
#Sintaxis y variables Python
numero_entero:int = 3 #Número entero
numero_decimales:float = 5.65 #Número en coma flotante
cadena_caracteres:str = "Hola" #Cadena de texto
booleana:bool = True #Booleana

print("Numero entero: " + str(numero_entero) + 
      "\nNúmero decimal en coma flotante: " + str(numero_decimales) + 
      "\nCadena de caracteres: " + cadena_caracteres +
      "\nVariable booleana: " + str(booleana))

print(f"Tipo de variable de {str(numero_entero)}:{type(numero_entero)}\n" +
      f"Tipo de variable de {str(numero_decimales)}:{type(numero_decimales)}\n" +
      f"Tipo de variable de {cadena_caracteres}:{type(cadena_caracteres)}\n"+
      f"Tipo de vatiable de {str(booleana)}:{type(booleana)}")