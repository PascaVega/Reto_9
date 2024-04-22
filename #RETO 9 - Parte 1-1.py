#RETO 9 - Parte 1-1
#Ejercicio tomado del punto 5 del reto 6
#Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

def introducir():
    #Ingreso de las variables
    capital_inicial : float = float(input("Ingrese el valor del préstamo. Ejemplo 1000000: "))
    interes : float = float(input("Ingrese el valor del interés por mes. Ejemplo 0.03: "))
    tiempo : float = float(input("Ingrese el tiempo del prestamo. Ejemplo 12: "))
    #Función Lambda
    capital_final = lambda capital_inicial, interes, tiempo: capital_inicial*(1+interes)**tiempo
    #Imprimir el resultado
    capitalFinal = capital_final(capital_inicial, interes, tiempo)
    print(f"El capital final del prestamo será de {capitalFinal}")

def continuar() -> int:
    #El usuario decide si desea continuar
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

#Iniciar el código
if __name__ == "__main__":
    print("Programa para determinar el capital final de un préstamo con interés compuesto")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/