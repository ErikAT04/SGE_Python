def fizz_buzz(cad1:str, cad2:str) -> int:
    numFin:int = 0
    for i in range(1, 101):
        if (i%15==0): #Es divisible por 3 y 5 a la vez
            print(cad1+cad2)
        elif (i%3==0): #Es divisible por 3 pero no por 5
            print(cad1)
        elif (i%5==0): #Es divisible por 5 pero no por 3
            print(cad2)
        else: #Ninguna de las anteriores
            print(i)
            numFin += 1 #Suma 1 cada vez que no imprime ninguna cadena, es decir, cuando se imprima el número
    return numFin

print(fizz_buzz("Fizz", "Buzz")) #Debería salir 53 mientras no se toque el for