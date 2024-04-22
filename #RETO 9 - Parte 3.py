#RETO 9 - Parte 3
#Escriba una función recursiva para calcular la operación de la potencia.

def introduccion():
  #Se introducen las variables
  base : float = float(input("Ingrese la base. Ejemplo 5.25: "))
  expo : int = int(input("Ingrese el exponente (natural). Ejemplo 5: "))
  return base,expo

def potencia(base,expo)  -> float:
  if expo == 0:
    #Caso base
    return 1
  else:
    #Se multiplica la base por la potencia(base, expo-1)
    return base * potencia(base, expo - 1)
  
def continuar():
  #El usuario decide si desea continuar
  opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
  return opcion

#Incia el código
if __name__ == "__main__":
  print("Programa para conocer la potencia de un numero utilizando funciones recursivas.")
  base,expo = introduccion()
  potenc = potencia(base,expo)
  #Se imprime el resultado
  print(f"La potencia de {base} elevado a {expo} es {potenc}")
  while True:
    opcion = continuar()
    if opcion == 2:
      break
    #Se verifica que no se usen otro tipo de respuestas
    elif opcion != 1 and 2:
      print("SintaxError")
      break

# ! /\|=\/