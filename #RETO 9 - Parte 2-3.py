#RETO 9  - Parte 1-1
#Ejercicio tomado  del punto 7 del taller 1
#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: 
#Promedio, mediana, promedio multiplicativo, ordenar los números de forma ascendente, ordenar los números de forma descendente, potencia del mayor número elevado al menor número, raíz cúbica del menor número.

#Se importa la libreria
from ordenar import ordenar_numeros

def introducir():
    #Se introducen los números
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    #Se envian los números a la función
    desarrollo(num1,num2,num3,num4,num5)

def desarrollo(*nums):
    #Se ordenan los núemros en una lista
    numeros = ordenar_numeros(*nums)
    print(f"Números de forma ascendente: {numeros}")

    #Se crea una lista de forma descendente y se imprime
    numeros_descendentes = [numeros[4],numeros[3],numeros[2],numeros[1],numeros[0]]
    print(f"Números de forma descendente: {numeros_descendentes}")

    #Se eleva a la potencia
    potencia : float = numeros[4]**numeros[0]
    print(f"potencia del mayor número elevado al menor número: {potencia}")

    #Se obtiene la raiz
    raiz : float = numeros[0] ** (1/3)
    print(f"La raiz cúbica del número menor: {raiz}")

def continuar() -> int:
    #El usuario decide si desea continuar
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

#Inicia el programa
if __name__ == "__main__":
    print("Ingrese cinco número para realizar determinadas operaciones.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break
# ! /\|=\/