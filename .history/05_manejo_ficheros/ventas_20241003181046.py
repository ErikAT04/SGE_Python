import os

file_name = "ventas.txt"

opt = -1
while(opt!=0):
    try:
        print("Escribe una opción:\n",
              "1: Añadir producto\n",
              "2: Consultar producto\n",
              "3: Actualizar producto\n",
              "4: Borrar producto\n",
              "5: Mostrar todos los productos\n",
              "6: Calcular venta total\n",
              "7: Calcular la venta por producto"
              "8: Salir")
        opt = int(input("Escribe la opción: "))
        match(opt):
            case 1:
                nombre = input("Escribe el nombre del producto")
                cantidad = int(input("Escribe la cantidad en stock: "))
                precio = float(input("Escribe el precio del producto: "))
                with open(file_name, "w") as file:
                    file.write(f"Nombre: {nombre} ; Stock: {cantidad} ; Precio: {precio}")
                    file.newlines()
                print("Añadido correctamente")
            case 2:
                nombre = input("Escribe el nombre del producto a consultar")
                isThere:bool = False
                with open(file_name, "r") as file:
                    content = file.readlines()
                    for s in content:
                        if nombre in s:
                            print(s)
                            isThere = True
                
                if isThere==False:
                    print("No se ha encontrado el producto")
            case 3:
                nombre = input("Escribe el nombre del producto")
                lugar:int = -1
                with open(file_name, "r") as file:
                    content = file.readlines()
                    for s in 0..len(content):
                        if nombre in content[s]:
                            lugar = s
                
                if (lugar!=-1):
                    cantidad = int(input("Escribe la cantidad en stock: "))
                    precio = float(input("Escribe el precio del producto: "))
                    with open(file_name, "w") as file:
                        file.writelines(f"Nombre: {nombre} ; Stock: {cantidad} ; Precio: {precio}")[lugar]
                    print("Actualizado")
                else:
                    print("No se ha encontrado el producto en la lista")
            case 4:
                nombre = input("Escribe el nombre del producto a borrar: ")
                exists:bool = False #Esta variable muestra si existe o no ese producto
                content
                with open(file_name, "r") as fileRead:
                    content = fileRead.readlines()
                    with open(file_name, "w") as fileWrite: 
                        for s in content:
                            if nombre in s:
                                exists = True
                            else:
                                fileWrite.write(s)
                            
                if(exists):
                    print("Borrado correctamente")
                else:
                    print("No se ha encontrado ese nombre en las ventas")
                    
            case 5:
                print("Lista de productos: ")
                with open(file_name, "r"):
                    content = fileRead.readlines()
                    for s in content:
                        print(s)
            case 6:
                print("Venta total:")
                with open(file_name, "r"):
                    content = fileRead.readlines()
                    for s
            case 7:
                print("Venta por producto: ")
            case 8:
                print("¡Hasta luego!")
                os.remove(file_name)
            case __:
                print("Opción no válida")
    except:
        print("El valor introducido debería ser numérico... Iniciando de vuelta.")