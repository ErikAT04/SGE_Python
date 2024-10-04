import os

file_name = "ventas.txt"

opt = -1
while(opt!=8):
    try:
        print("Escribe una opción:\n",
              "1: Añadir producto\n",
              "2: Consultar producto\n",
              "3: Actualizar producto\n",
              "4: Borrar producto\n",
              "5: Mostrar todos los productos\n",
              "6: Calcular venta total\n",
              "7: Calcular la venta por producto\n",
              "8: Salir")
        opt = int(input("Escribe la opción: "))
        match(opt):
            case 1:
                nombre = input("Escribe el nombre del producto: ")
                cantidad = int(input("Escribe la cantidad en stock: "))
                precio = float(input("Escribe el precio del producto: "))
                with open(file_name, "a") as file: ##"a" = Append, es decir, añade el contenido al final del documento cada vez que entra
                    file.write(f"Nombre: {nombre};Stock: {cantidad};Precio: {precio}\n") #Guarda una línea entera con este modelo
                print("Añadido correctamente")
            case 2:
                nombre = input("Escribe el nombre del producto a consultar: ")
                isThere:bool = False #Booleana que guarda si ha encontrado el producto o no
                with open(file_name, "r") as file:
                    content = file.readlines() #Genera una lista de strings con el contenido del archivo
                    for s in content:
                        if f"Nombre: {nombre};" in s: #Si encuentra el patrón Nombre: (nombreProducto);, imprime el número y cambia a True la booleana
                            print(s)
                            isThere = True
                
                if isThere==False: #Si no ha cambiado la booleana, dice que no se ha encontrado el producto
                    print("No se ha encontrado el producto")
            case 3:
                nombre = input("Escribe el nombre del producto: ")
                lugar:int = -1 #Guarda el lugar
                iterator = 0 #Hago un iterador para que aumente en función del forEach
                listadoProd=[] #Creo otra lista
                with open(file_name, "r") as file:
                    while s:= file.readline():
                        listadoProd.append(s) #Añade el contenido a la lista
                        if f"Nombre: {nombre};" in s: #Si encuentra el nombre, guarda el valor del iterador en ese momento en la variable lugar
                            lugar = iterator
                        iterator+=1
                
                if (lugar!=-1): #Si el lugar ha cambiado (no es -1), actualiza el lugar
                    cantidad = int(input("Escribe la cantidad en stock: "))
                    precio = float(input("Escribe el precio del producto: "))
                    listadoProd[lugar] = f"Nombre: {nombre};Stock: {cantidad};Precio: {precio}"
                    with open(file_name, "w") as file: #Abre el archivo de vuelta en modo escritura (borra el contenido del documento antes de escribir)
                        for s in listadoProd: #Escribe otra vez la lista entera, con los cambios realizados
                            file.write(s)
                    print("Actualizado")
                else:
                    print("No se ha encontrado el producto en la lista")
            case 4:
                nombre = input("Escribe el nombre del producto a borrar: ")
                exists:bool = False #Esta variable muestra si existe o no ese producto buscado
                listadoProd:list = [] # Listado de productos
                with open(file_name, "r") as file: #Se abre el archivo en modo lectura
                    while s := file.readline(): #Mientras s se iguale a la siguiente linea (es decir, que haya líneas disponibles)
                        if f"Nombre: {nombre};" in s: #Si existe el nombre a buscar, no se guarda
                            exists = True
                        else: #Si no, añade de vuelta a la lista
                            listadoProd.append(s)
                
                if(exists): # Si existe el producto:
                    with open(file_name, "w") as fileWrite: #Se abre la lista de nuevo en modo escritura (borra el contenido del documento)
                        for s in listadoProd: #Y añade el contenido guardado en la lista, dejando0 de lado el producto
                            fileWrite.write(s)
                    print("Borrado correctamente")
                else:
                    print("No se ha encontrado ese nombre en las ventas")
                    
            case 5:
                try:
                    print("Lista de productos: ")
                    with open(file_name, "r") as file: #Abre el archivo en modo lectura
                        while s := file.readline(): #Mientras encuentre una línea con texto la imprime por pantalla
                            print(s)
                except:
                    print("No se ha encontrado productos en la lista")
            case 6:
                totalVendido = 0. #Float de 0 que guarda el total vendido (precio*stock de todos los objetos)
                with open(file_name, "r") as file:
                    while s:=file.readline():
                        stock = s.split(";")[1] #Aquí saca "Stock: X"
                        precio = s.split(";")[2] #Aquí saca "Precio: X"
                        
                        stock = int(stock[7:]) #Quita "Stock: ", quedándose con el stock
                        precio = float(precio[8:]) #Quita "Precio: ", quedándose solo con el precio del objeto

                        totalVendido += (stock*precio) #Se suma el stock por el precio al total vendido
                print(f"Venta total: {totalVendido}")
            case 7:
                print("Venta por producto: ")
                with open(file_name, "r") as file:
                    while s:=file.readline():
                        nombre = s.split(";")[0] #Saca "Nombre: ", aunque no lo edite
                        stock = s.split(";")[1] #Aquí saca "Stock: X"
                        precio = s.split(";")[2] #Aquí saca "Precio: X"


                        stock = int(stock[7:]) #Quita "Stock: ", quedándose con el stock
                        precio = float(precio[8:]) #Quita "Precio: ", quedándose solo con el precio del objeto


                        total=stock*precio

                        print(f"{nombre};Stock: {stock};Precio: {precio}; Total de venta: {total}") #Imprime la linea entera mas el total de venta
            case 8:
                print("¡Hasta luego!")
                os.remove(file_name) #Esto lo que hace es borrar el archivo directamente
            case _: #Si la opción no es ninguna de las dadas:
                print("Opción no válida")
            
    except:
        print("El valor introducido debería ser numérico... Iniciando de vuelta.")
    print() #Salto de línea por tema de estética
    