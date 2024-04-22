#RETO 9 - Parte 1-2
#Ejercicio tomado del punto 6 del reto 6
#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día.
#Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

def introducir():
    #Introducir las variables
    dias : float = float(input("Ingrese el número de días transcurridos. Ejemplo 5: "))
    contagiados : float = float(input("Ingrese el número de contagiados iniciales. Ejemplo 24: "))
    #Función Lambda
    contagiados_finales = lambda dias, contagiados: contagiados*2**dias
    #Imprimir el resultado
    contagiadosFinales = contagiados_finales(dias,contagiados)
    print(f"El numero de contagiados después de {dias} dia(s) es de {contagiadosFinales}")
    return
 
def continuar() -> int:
    #El usuario decide si desea continuar
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

#Inicia el programa
if __name__ == "__main__":
    print("Programa para determinar el número de contagiados de COVID-19")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/