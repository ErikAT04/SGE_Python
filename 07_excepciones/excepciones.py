#CONTROL DE EXCEPCIONES:
try: #Inicio de la búsqueda de excepciones
    numero:int = int(input("Escribe un número: ")) #Si se escribe una letra, salta una excepcion
    print("Tu numero es " + numero) #Esto solo sale si no salta la excepcion
except: #Salto al control de excepciones
    print("No es un número")
finally: #Da igual si salta o no la excepción, saltará lo siguiente al finalizar.
    print("Se ha terminado el control de la excepción")