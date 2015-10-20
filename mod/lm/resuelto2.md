---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Solución boletín 2: Ejercicios alternativas

1. Realiza un programa que pida dos números 'a' y 'b' e indique si su suma es positiva, negativa o
cero.		

		num1=int(raw_input("Número 1:"))
		num2=int(raw_input("Número 2:"))		

		if num1+num2>0:
			print "Suma positiva"
		elif num1+num2<0:
			print "Suma negativa"
		else:
			print "Suma es 0"		

2. Realiza un programa que pida una nota numéricas enteras e imprima sus equivalentes en texto (0-2 => MD, 3-4 => I, 5 => Suf, 6 => B, 7-8 => Not, 9-10 => Sob, otro => Error)

		nota=int(raw_input("Nota:"))		

		if nota>=0 and nota<=2:
			print "MD"
		elif nota==3 or nota==4:
			print "I"
		elif nota==5:
			print "Suf"
		elif nota==6:
			print "B"
		elif nota==7 or nota==8:
			print "Not"
		elif nota==9 or nota==10:
			print "Sob"
		else:
			print "Error"

3. Escribe un programa que lea un número e indique si es par o impar.

		num=int(raw_input("Número:"))		

		if num%2==0:
			print "Número par"
		else:
			print "Número impar"

4. Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

		mes=int(raw_input("Mes:"))		

		if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
			print "31 días"
		elif mes==4 or mes==6 or mes==9 or mes==11 :
			print "30 días"
		elif mes==2:
			print "28 o 29 días"
		else:
			print "Mes incorrecto"


5. Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error.

		usuario=raw_input("Usuario:")
		clave=raw_input("Contraseña:")		

		if usuario=="pepe" and clave=="asdasd":
			print "Has entrado en el sistema"
		else:
			print "Error"

6. Algoritmo que pida tres números y los muestre ordenados.

		num1=int(raw_input("Número 1:"))
		num2=int(raw_input("Número 2:"))
		num3=int(raw_input("Número 3:"))		

		if num1>=num2 and num2>=num3:
			print num1,num2,num3
		if num1>=num3 and num3>num2:
			print num1,num3,num2
		if num2>num1 and num1>=num3:
			print num2,num1,num3
		if num2>=num3 and num3>num1:
			print num2,num3,num1
		if num3>num1 and num1>=num2:
			print num3,num1,num2
		if num3>num2 and num2>num1:
			print num3,num2,num1

7. Realiza un programa en python que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

	* Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
    * Nota 2: Si el número del dado introducido es menor que 1 ó mayor que 6, se mostrará el mensaje: "ERROR: número incorrecto.".

	Ejemplo:
	
	*Introduzca número del dado: 5*
	*En la cara opuesta está el "dos".*

		dado=int(raw_input("Número del dado:"))		

		if dado==1:
			print "Seis"
		elif dado==2:
			print "Cinco"
		elif dado==3:
			print "Cuatro"
		elif dado==4:
			print "Tres"
		elif dado==5:
			print "Dos"
		elif dado==6:
			print "Uno"
		else:
			print "Error: número incorrecto"

8.  Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniedno en cuenta los siguiente:

	* Si se cumple Pitágoras entonces es triángulo rectángulo
	* Si sólo dos lados del triángulo son iguales entonces es isósceles.
	* Si los 3 lados son iguales entonces es equilátero.
	* Si no se cumple ninguna de las condiciones anteriores, es escaleno.


	Solución:

		lado1=float(raw_input("A:"))
		lado2=float(raw_input("B:"))
		lado3=float(raw_input("C:"))				

		if lado1**2==(lado2**2+lado3**2):
			print "Rectangulo"
		if lado1==lado2 and lado2==lado3:
			print "Equilátero"
		elif lado1==lado2 or lado1==lado3 or lado2==lado3:
			print "Isósceles"
		else:
			print "Escaleno"

9. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

		year=int(raw_input("Año:"))		

		if year%4==0 and year%100!=0 or year%400==0:
			print "Bisiesto"
		else:
			print "No bisiesto"

10. Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.

		letra=raw_input("Letra:")		

		if letra>="A" and letra<="Z":
			print "Mayuscula"
		else:
			print "No mayuscula"

[Volver](index)