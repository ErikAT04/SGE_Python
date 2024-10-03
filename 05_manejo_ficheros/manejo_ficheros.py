import os #Se importa la librería de manejo de archivos

file_name = "fichero.txt" #El nombre del fichero es el lugar en el que se encuentra desde la raíz del proyecto + su nombre
#Si no encuentra un archivo, lo crea.

with open(file_name, "w") as file: #Abro el fichero en modo escritura "w" = "write"
    file.write("Prueba\n")
    file.write("Nombre\n")
    file.write("a\n")

with open(file_name, "r") as file: #Abro el fichero en modo lectura "r" = "read"
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open(file_name, "w") as file:
    file.flush() #File.flush() sirve para borrar todo el contenido del fichero

os.remove(file_name) #Con esto se elimina el archivo