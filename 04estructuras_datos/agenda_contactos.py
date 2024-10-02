def verificarNum(numTlf) -> bool:
    return numTlf.isDigit() and numTlf>0 and len(numTlf)<=9 

def insertar(numTlf, nombre, agenda):
    if(numTlf in agenda):
        print("Ya existe ese número en la agenda")
    else:
        agenda[numTlf] = nombre
        print(f"{nombre}, de teléfono {numTlf}, añadido correctamente")

def actualizar(numTlf, nombre, agenda):
    if(numTlf in agenda):
        agenda[numTlf] = nombre
        print("Cambio realizado")
    else:
        print("No existe ese número")

def borrar(numTlf, agenda):
    if(numTlf in agenda):
        agenda.pop(numTlf)
        print("Borrado correctamente")
    else:
        print("No existe ese número en la agenda")

def listar(agenda):
    print("Listado de contactos")
    for x in agenda:
        print(x)

agenda:dict = {
}
opt:int = -1
while(opt!=0):
    try:
        print("Elige una opción: \n1.Añadir un contacto\n2.Actualizar datos de un contacto\n3.Eliminar un contacto\n4.Imprimir los contactos\n0.Salir")
        opt = int(input("Opción elegida: "))
        match(opt):
            case 1:
                nombre = input("Escribe el nombre: ")
                numtlf:int = 0
                while(numtlf == 0):
                    numtlf = input("Escribe el número de teléfono: ")
                    if (verificarNum(numtlf)):
                        insertar(int(numtlf), nombre, agenda)
                    else:
                        print("Formato de número no válido")
                        numtlf=0
            case 2:
                numtlf:int = 0
                while(numtlf == 0):
                    try:
                        numtlf = int(input("Escribe el número de teléfono: "))
                        contacto:Contacto = buscarContacto(numtlf, agenda)
                        if (contacto != any):
                            print("No se ha encontrado un contacto con ese número")
                        else:
                            nombre = input("Escribe un nuevo nombre para este número: ")
                            contacto.nombre = nombre
                            actualizarContacto(contacto, agenda)
                    except:
                        print("El valor solo puede ser numérico")
                        numtlf = 0
            case 3:
                numtlf:int = 0
                while(numtlf == 0):
                    try:
                        numtlf = int(input("Escribe el número de teléfono: "))
                        contacto:Contacto = buscarContacto(numtlf, agenda)
                        if (contacto != any):
                            print("No se ha encontrado un contacto con ese número")
                        else:
                            eliminarContacto(contacto, agenda)
                    except:
                        print("El valor solo puede ser numérico")
                        numtlf = 0
            case 4:
                agenda.sort()
                for contacto in agenda:
                    print (contacto.nombre + " " + contacto.numtlf)
            case 0:
                print("¡Hasta luego!")
            case _:
                print("Opción no válida")
    except:
        print("Tiene que ser un valor no numérico")
        opt = -1