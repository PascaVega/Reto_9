#RETO 9  - Parte 1-2
#Ejercicio tomado  del punto 7 del taller 1
#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: promedio multiplicativo

def introducir():
    #Se introducen los números
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    #Los números se ingresan como arg a la función
    promedio_multiplicativo(num1,num2,num3,num4,num5)

def promedio_multiplicativo(*arg)-> float:
    #Nueva variable para el promedio
    promul : float = 1
    for num in arg:
        #Cada número se va multiplicando hasta conseguir el promedio
        promul *=  num
    #Al finalizar el promedio se divide en 5
    promul = promul/5
    print(f"Promedio Multiplciativo: {promul}")
    return
   
def continuar() -> int:
    #El usuario decide si quiere continuar
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