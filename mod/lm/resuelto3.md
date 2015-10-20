---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Solución boletín 3: Ejercicios bucles

1. Realiza un programa en python que muestre la tabla de multiplicar, convierte este pseudocódigo en el programa python:

		INICIO
		MIENTRAS numero < 0 O numero > 9
		  ESCRIBIR "Dame un numero entre 0 y 9"
		  LEER numero 
		  SI numero > 9 ENTONCES
		    ESCRIBIR "Numero demasido alto"
		  SINO 
		    SI numero < 0 ENTONCES
		      ESCRIBIR "Numero demasiado bajo"
		    FINSI
		  FIN_SI
		FIN_MIENTRAS
		PARA i=0 HASTA 15 con INCREMENTO 1 
		  ESCRIBIR numero"X"i"="numero*i
		FIN_PARA
		FIN

		num=int(raw_input("Dame un numero entre 0 y 9:"))
		
		while num<0 or num>9:
			if num>9:
				print "Numero demasido alto"
			else:
				print "Numero demasido bajo"
			num=int(raw_input("Dame un numero entre 0 y 9:"))
		for i in xrange(1,16):
	print "%d*%d=%d"%(num,i,i*num)	

2. Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),

		num=int(raw_input("Número:"))
		fact=1
		for i in xrange(2,num+1):
			fact=fact*i
		print fact

3. Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.

		secreto=int(raw_input("Número secreto:"))
		num=int(raw_input("Número:"))
		while num!=secreto:
			if num>secreto:
				print "El número es menor"
			else:
				print "El número es mayor"
			num=int(raw_input("Número:"))
		print "Has acertado"

4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

		suma=0
		cont=0
		num=int(raw_input("Número:"))
		while num!=0:
			cont=cont+1
			suma=suma+num
			num=int(raw_input("Número:"))
		media=float(suma)/cont
		print "La suma es %d y la media es %f"%(suma,media)

5. Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y
'CONSONANTE' si no, el programa termina cuando se introduce un *espacio*.

		letra=raw_input("Letra:")
		while letra!=" ":
			if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
				print "Vocal" 
			else:
				print "Consonante"
			letra=raw_input("Letra:")

6. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

		num1=int(raw_input("Número:"))
		num2=int(raw_input("Número:"))
		for i in xrange(num1,num2+1):
			if i%2==0:
				print i,

7. Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

		for num1 in xrange(1,6):
			for num2 in xrange(1,11):
				print "%d*%d=%d"%(num1,num2,num1*num2)

8. Escribe un programa que lea una lista de diez números y determine cuántos
son positivos, y cuántos son negativos.

		cont_pos=0
		cont_neg=0;
		for cont in xrange(1,11):
			num=int(raw_input("Número:"))
			if num>=0:
				cont_pos=cont_pos+1
			else:
				cont_neg=cont_neg+1
		print "%d positivos,%d negativos"%(cont_pos,cont_neg)	

9. Escribe un programa que dados dos números, uno real (base) y un entero
positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia (**).

		base=float(raw_input("Base:"))
		exp=int(raw_input("Exponente:"))
		potencia=1
		for cont in xrange(1,exp+1):
			potencia=potencia*base
		print "Potencia=%f"%potencia

10. Escribe un programa que diga si un número introducido por teclado es o no
primo. Un número primo es aquel que sólo es divisible entre él mismo y la
unidad.

		num=int(raw_input("Número:"))
		primo = True
		for cont in xrange(2,num):
			if num%cont==0:
				primo=False
		if primo:
			print "Es primo"
		else:
			print "No es primo"

[Volver](index)