# EJERCICIO 1

print("Hola Mundo!")

# EJERCICIO 2

nombre = input("Ingrese su nombre:")
saludo = f"Bienvenido {nombre} !!!!"

print(saludo)

# EJERCICIO 3

nombre = input("Ingrese su Nombre:")
apellido = input("Ingrese su Apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su lugar de residencia:")

print(f"Su nombre y apellido son {nombre} {apellido}, su edad es {edad} y su lugar de residencia es en: {residencia}")

# EJERCICIO 4

pi = 3.141592653589793
radio = float(input("Ingrese el radio de un círculo:"))
superficie = pi * radio ** 2
perimetro = pi * radio * 2

print(f"Su area es {superficie} y el perímetro es {perimetro}")

# EJERCICIO 5

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = round(segundos / 60, 2)

print(f"{segundos} segundos son {horas} horas")

# EJERCICIO 6

numero = int(input("Ingrese un numero entero: "))
var0 = numero * 0
var1 = numero * 1
var2 = numero * 2
var3 = numero * 3
var4 = numero * 4
var5 = numero * 5
var6 = numero * 6
var7 = numero * 7
var8 = numero * 8
var9 = numero * 9
var10= numero * 10

print(f"""La tabla de multiplicar de {numero} es:
      {numero} * 0 = {var0}
      {numero} * 1 = {var1}
      {numero} * 2 = {var2}
      {numero} * 3 = {var3}
      {numero} * 4 = {var4}
      {numero} * 5 = {var5}
      {numero} * 6 = {var6}
      {numero} * 7 = {var7}
      {numero} * 8 = {var8}
      {numero} * 9 = {var9}
      {numero} * 10 = {var10}""")

# EJERCICIO 7

num1 = int(input("Ingrese un numero entero distinto de 0: "))
num2 = int(input("Ingrese otro numero entero distinto de 0: "))

print(f"""El resultado de sumar {num1} y {num2} es igual a {num1 + num2}.
          El resultado de dividir {num1} entre {num2} es igual a {num1 / num2}.
          El resultado de multiplicar {num1} por {num2} es igual a {num1 * num2}.
          El resultado de restar {num1} y {num2} es igual a {num1 - num2}.""")

# EJERCICIO 8

altura = float(input("Ingrese su altura(mts.): "))
peso = float(input("Ingrese su peso (kg.): "))
imc = peso / (altura ** 2)

print(f"Su IMC es: {imc}")

# EJERCICIO 9

tempC = int(input("Ingrese la temperatura en ºC: "))

print(f"La temperatura en grados Farenheit es {(9/5 * tempC) + 32 }")

# EJERCICIO 10

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero: "))
num3 = float(input("Ingrese un tercer numero: "))

print(f"El promedio de los 3 números es: {(num1 + num2 + num3)/ 3}")