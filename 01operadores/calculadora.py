try:
    num1:int = int(input("Escribe el primer número: "))
    num2:int = int(input("Escribe el segundo número: "))
    print(f"Suma: {num1+num2}")
    print(f"Resta: {num1-num2}")
    print(f"Multiplicación: {num1*num2}")
    print(f"División: {int(num1/num2)}")
    print(f"Resto: {num1%num2}")
except: 
    print("Eso no era un número.")