def verificarNum(numTlf) -> bool:
    return numTlf>0 and numTlf<=999999999 

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
                numtlf = 0
                while(numtlf == 0):
                    print("Escribe el número de teléfono:")
                    numtlf = int(input())
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
                        nombre = input("Escribe un nuevo nombre para este número: ")
                        actualizar(numtlf, nombre, agenda)
                    except:
                        print("El valor solo puede ser numérico")
                        numtlf = 0
            case 3:
                numtlf:int = 0
                while(numtlf == 0):
                    try:
                        numtlf = int(input("Escribe el número de teléfono: "))
                        borrar(numtlf, agenda)
                    except:
                        print("El valor solo puede ser numérico")
                        numtlf = 0
            case 4:
                for contacto, telf in agenda.items():
                    print(f"{contacto} : {telf}")
            case 0:
                print("¡Hasta luego!")
            case _:
                print("Opción no válida")
    except:
        print("Tiene que ser un valor numérico")
        opt = -1