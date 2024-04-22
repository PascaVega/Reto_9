#RETO 9  - Parte 1-1
#Ejercicio tomado  del punto 7 del taller 1
#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: Promedio

def introducir():
    #Introducir las variables
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    #Se ingresan los datos como *args
    promedio(num1,num2,num3,num4,num5)

def promedio(*args)-> float:
    #Se define una nueva variable
    prom : float = 0
    for num in args:
        #Se havce el promedio como una suma de fracciones
        prom +=  num/5
    print(f"Promedio: {prom}")
    return
  
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