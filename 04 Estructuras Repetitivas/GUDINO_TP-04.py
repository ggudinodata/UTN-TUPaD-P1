# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = input("Ingrese un número entero ")
contador = 0

for i in num:
    contador += 1

print(f"El número {int(num)} tiene {contador} dígito/s.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero "))
num2 = int(input("Ingrese un segundo número entero "))
sumador = 0

if (num1 < num2) and (num2 - num1 >= 2):
    for i in range(num1 + 1, num2 ):
        sumador += i
elif num1 >= num2  and (num1 - num2 >= 2):
    for i in range(num2 + 1, num1 ):
        sumador += i
else:
    print("La distancia entre los dos números no es la suficiente para poder hacer el cálculo")

print(f"La suma de los número entre {num1} y {num2} es {sumador}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

acumulador = 0
num = 1

while num != 0:
    num = int(input("Ingrese un número entero "))
    acumulador += num

print(f"El total acumulado fue de {acumulador}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint

numero_aleatorio = randint(0, 9)
num = 10
contador = 0

while num != numero_aleatorio:
    num = int(input("Advine cual es el número entero (0 al 9)"))
    contador += 1

print(f"Ud. adivinó! el número {numero_aleatorio} en {contador} intento/s.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

sumador = 0
limite = int(input("Ingrese el número límite al que quiere hacer la sumatoria "))

for i in range(0, limite+1):
    sumador += i

print(f"El valor acumulado de la suma entre 0 y {limite} es {sumador}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador_par = 0
contador_impar = 0
contador_neg = 0
contador_pos = 0

for i in range(0, 100):
    num = int(input("Ingrese un número entero "))
    if num % 2 == 0:
        contador_par += 1
        if num >= 0:
            contador_pos += 1
        else:
            contador_neg += 1
    else:
        contador_impar += 1
        if num >= 0:
            contador_pos += 1
        else:
            contador_neg += 1

print(f"Números pares: {contador_par}, Números impares: {contador_impar}, Números positivos: {contador_pos}, Números negativos: {contador_neg}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

sumador = 0
rango = 100

for i in range(rango):
    num = int(input("Ingrese un número entero "))
    sumador += num

print(f"La media de los números ingresados es {sumador / rango}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un número de dos dígitos o mas ")
num_inv =""

for i in range(len(num)-1, -1, -1):
    num_inv = num_inv + num[i]
    
print(num_inv)