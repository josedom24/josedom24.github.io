---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Solución boletín 1: Ejercicios sencillos

1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

		nombre=raw_input("Dime tu nombre:")
		print "Hola %s" % nombre

2. Calcular el perímetro y área de un rectángulo dada su base y su altura.

		base=float(raw_input("Dime la base:"))
		altura=float(raw_input("Dime la altura:"))
		perimetro = 2*base + 2*altura
		area = base * altura
		print "Resultado: Area=%.2f Perimetro=%.2f" % (area,perimetro)

3. Calcular el perímetro y área de un círculo dado su radio.

		import math
		radio=float(raw_input("Dime el radio:"))
		print "Resultado: Area=%.2f Perimetro=%.2f" % (math.pi*radio**2,2*math.pi*radio)		

4. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

		import math
		cateto1=float(raw_input("Dime el cateto1:"))
		cateto2=float(raw_input("Dime el cateto2:"))
		print "Hipotenusa=%.2f" % math.sqrt(cateto1**2+cateto2**2)

5. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

		num1=float(raw_input("Numero1:"))
		num2=float(raw_input("Numero2:"))
		print "Suma:%d,resta:%d,multiplicacion:%d,division:%.2f"%(num1+num2,num1-num2,num1*num2,float(num1)/num2)

6. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.

		palabra=raw_input("Dime una palabra:")
		print (palabra+" ")*1000

7. Escribir un programa que le pregunte al usuario una cantidad de euros, una tasa de interés y un número de años y muestre como resultado la cantidad final a pagar. La fórmula a utilizar es:

		Cn = C * (1 + x/100) ^ n
	
	Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

		cant=float(raw_input("Euros:"))
		interes=float(raw_input("Interes:"))
		year=int(raw_input("Years:"))
		a_pagar=cant*(1+interes/100)**year
		print "A pagar %.2f euros." % a_pagar

8.  Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 

		F = 9/5 * C + 32.
 
		gf=float(raw_input("Grados Fahrenheit:"))
		gc=(gf*5/9)-32
		print "Grados C:%.2f" % gc	

9. Calcular la media de tres números pedidos por teclado.

		num1=float(raw_input("Numero1:"))
		num2=float(raw_input("Numero2:"))
		num3=float(raw_input("Numero3:"))
		print "Media:%.2f" % ((num1+num2+num3)/3)

10. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

	Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

		minutos=int(raw_input("Minutos:"))
		print "Horas:%d - Minutos:%d" % (minutos/60,minutos%60)

[Volver](index)
