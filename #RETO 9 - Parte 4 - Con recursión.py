#RETO 9 - Parte 4 - Con recursión
import time

def fibonacci(n : int)-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fibonacci(n-1)+fibonacci(n-2)  
  
def tiempo(num) -> float:
  #Medir tiempo que se demora en ejecutar la serie de un número
  start_time = time.time()
  serie = fibonacci(num)
  end_time = time.time()
  timer : float = end_time - start_time
  print(f"La serie de {num} es {serie}")
  return timer
  

if __name__ == "__main__":
  start_time_total : float = time.time()
  #Se definenen los números iniciales
  num_1 : int = 1
  num_2 : int = 2
  #La serie se hara hasta el número 49 y 50
  while num_1 < 50:
    #Se calcula el tiempo de dos series consecutivas para luego saber la diferencia de tiempo entre ellas
    serieFibo_1 = tiempo(num_1)
    serieFibo_2 = tiempo(num_2)
    tiempo_diferencia : float = serieFibo_2 - serieFibo_1
    #Se imprimen los resultados
    print(f"El tiempo de la serie entre {num_1} y {num_2} es de {tiempo_diferencia}, donde se demoro en la primera serie {serieFibo_1} y en la segunda {serieFibo_2}")
    num_1 += 1
    num_2 += 1
  end_time_total : float = time.time()
  timer_total : float = end_time_total - start_time_total
  print(f"El tiempo que se demoró el programa en terminar fue: {timer_total}")

# ! /\|=\/