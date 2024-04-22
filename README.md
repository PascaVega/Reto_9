# Reto 9
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Solución del reto
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se tomaron los siguientes ejercicios:
        <li>Punto 5 del reto 6: Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.</li>
        <li>Punto 6 del reto 6: Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.</li>
        <li>Punto 1 del reto 7: Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.</li>
    </td>
  </tr>
</table>

**Parte 1 - 1**
```python
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
```

**Parte 1 - 2**
```python
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
```

**Parte 1 - 3**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se tomaron los siguientes ejercicios:
        <li>Punto 7 del taller 1: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: Promedio</li>
        <li>Punto 7 del taller 1: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: promedio multiplicativo</li>
        <li>Punto 7 del taller 1: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: promedio, mediana, promedio multiplicativo, ordenar los números de forma ascendente, ordenar los números de forma descendente, potencia del mayor número elevado al menor número, raíz cúbica del menor número.</li>
    </td>
  </tr>
</table>

**Parte 2 - 1**
```python
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
```

**Parte 2 - 2**
```python
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
```

**Parte 2 - 3**
```python
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
```

**Función de ordenar números**
```python
#Funciones

def ordenar_numeros(num1,num2,num3,num4,num5):
    # Encontrar el primer número más pequeño y asignarlo a la primera posición
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        numeros = [num1, 0, 0, 0, 0]
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        numeros = [num2, 0, 0, 0, 0]
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        numeros = [num3, 0, 0, 0, 0]
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        numeros = [num4, 0, 0, 0, 0]
    else:
        numeros = [num5, 0, 0, 0, 0]

    # Encontrar el segundo número más pequeño y asignarlo a la segunda posición
    if (num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5) or numeros[0] == num1:
        if num2 <= num3 and num2 <= num4 and num2 <= num5:
            numeros[1] = num2
        elif num3 <= num2 and num3 <= num4 and num3 <= num5:
            numeros[1] = num3
        elif num4 <= num2 and num4 <= num3 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
        if num1 <= num3 and num1 <= num4 and num1 <= num5:
            numeros[1] = num1
        elif num3 <= num1 and num3 <= num4 and num3 <= num5:
            numeros[1] = num3
        elif num4 <= num1 and num4 <= num3 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
        if num1 <= num2 and num1 <= num4 and num1 <= num5:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num4 and num2 <= num5:
            numeros[1] = num2
        elif num4 <= num1 and num4 <= num2 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5:
        if num1 <= num2 and num1 <= num3 and num1 <= num5:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num3 and num2 <= num5:
            numeros[1] = num2
        elif num3 <= num1 and num3 <= num2 and num3 <= num5:
            numeros[1] = num3
        else:
            numeros[1] = num5
    else:
        if num1 <= num2 and num1 <= num3 and num1 <= num4:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num3 and num2 <= num4:
            numeros[1] = num2
        elif num3 <= num1 and num3 <= num2 and num3 <= num4:
            numeros[1] = num3
        else:
            numeros[1] = num4

# Encontrar el tercer número más pequeño y asignarlo a la tercera posición
    for i in range(2, 5):
        if numeros[i] == 0:
            smallest_remaining = min([num for num in [num1, num2, num3, num4, num5] if num not in numeros])
            numeros[i] = smallest_remaining

    return numeros
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Escriba una función recursiva para calcular la operación de la potencia.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, la base puede ser un número flotante, pero el exponente solo puede ser un número natural.</td>
  </tr>
</table>

**Parte 3**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este punto, se crearon dos programas con la misma función, con el fin de conocer la diferencia significativa de tiempo entre las series y ambos programas.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Conclusiones:</b> 
      <li>Con iteración el programa demoro aproximadamente 0.03344 segundos, lo que hizo que en ese tiempo no se evidenciara gran diferencia entre las series. </li>
      <li>Con recursión el programa demoro aproximadamente 0.03344 segundos, en donde la diferencia entre series comenzó a ser significativa a partir de la serie 39 (se demoró aproximadamente 10.27484 segundos), y desde este punto las series comenzaron a tardar cada vez más, hasta finalizar con la serie 50 con _ segundos. Y el programa finalizó con un tiempo de _ segundos, lo que aproximadamente son _ minutos.</li>
      <li>Por ende, para realizar la sucesión de Fibonacci el método más eficiente (debido a su rapidez) es la iteración.</li>
    </td>
  </tr>
</table>

**Parte 4 - Con recursión**
```python
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
```

**Parte 4 - Con iteración**
```python
#RETO 9 - Parte 4 - Con iteración
import time

def fibonacci(n : int)-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo
  
def tiempo(num) -> float:
  #Medir tiempo que se demora en ejecutar la serie de un número
  start_time = time.time()
  serie = fibonacci(num)
  end_time = time.time()
  timer : float = end_time - start_time
  print(f"La serie {num} es {serie}")
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Crear cuenta en stackoverflow y adjuntar imagen en el repo</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Perfil de Stack overflow: https://stackoverflow.com/users/24580456/ang%c3%a9lica-pascagaza <a href="https://stackoverflow.com/users/24580456/ang%c3%a9lica-pascagaza"></a>  </td>
  </tr>
</table>

[![Captura-de-pantalla-2024-04-22-133420.png](https://i.postimg.cc/V6M3MwW8/Captura-de-pantalla-2024-04-22-133420.png)](https://postimg.cc/348S5PqS)

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 6</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Crear un pefil en linkedin.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Link del perfil de Likedin www.linkedin.com/in/angélica-pascagaza-vega-186610305<a href="www.linkedin.com/in/angélica-pascagaza-vega-186610305"></a></td>
  </tr>
</table>
