"""
TÍTULO DEL PROGRAMA:
"""
# Comentario:
class StrTypeError(Exception):
    pass


def process_params(parameters: list):
        
    if len(parameters) < 3:
        raise IndexError() # Salta una excepción si la lista tiene menos de 3 elementos
    elif parameters[1] == 0:
        raise ZeroDivisionError() # Salta una excepción si el valor del segundo hueco de la lista es igual a 0
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto") # Salta una excepción si el tipo de valor que guarda el tercer elemento es String. Pasa como parámetro en el rise una cadena de caracteres
    
    print(parameters[2]) # Imprime el tercer valor de la lista
    print(parameters[0]/parameters[1]) # Imprime la división primer valor entre el segundo
    print(parameters[2]+5) # Imprime la suma del tercer valor mas 5


try:   
    process_params([23, 2, 2, 45]) #Llama a la función y le pasa una lista de 4 valores
except IndexError as e: # Si se da el caso de que la lista tiene menos de 3 valores:
    print("La lista debe tener más de 2 elementos")
except ZeroDivisionError as e: # Si se da el caso de que el segundo valor es 0:
    print("El segundo elemento de la lista no puede ser cero")
except StrTypeError as e: # Si se da el caso de que el valor 3 es de tipo String:
    print(f"{e}")
except Exception as e: # Imprime una excepción general que no se haya controlado antes
    print(f"Se ha producido un error inesperado: {e}")
else: # Si no ha habido ninguna excepción:
    print("No se ha producido ningún error")
finally: # Aquí llega haya saltado o no una excepción, e imprime lo siguiente:
    print("El programa finaliza sin detenerse")


print("Fin del programa")



