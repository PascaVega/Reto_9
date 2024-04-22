#RETO 9 - Parte 1-3
#Ejercicio tomado del punto 1 del reto 7
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#Se  define una variable inicial
n : int = 1

#Inicia el programa
if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")

    #Se usa el ciclo while para imprimir los números
    while n <= 100:
        #Función Lambda
        cuadrado = lambda n: n**2
        #Nueva variable para imprimir los cuadrados
        m : int = cuadrado(n)
        print(f"El cuadrado de {n} es {m}")
        n += 1

# ! /\|=\/