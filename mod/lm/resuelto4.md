---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Boletín 4: Ejercicios listas

1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.

		num=int(raw_input("Número:"))
		lista=[]
		while num>0:
			lista.append(num)
			num=int(raw_input("Número:"))		

		print max(lista)
		for n in lista:
			if n % 2 ==0:
				print n

2. Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

		num=int(raw_input("Número de palabras:"))
		lista=[]
		for i in xrange(1,num+1):
			lista.append(raw_input("Palabra:"))
			
		print lista

3. Dada una lista de números enteros (guarda la lista en una variable) y un entero *k*, escribir un programa que:

	* Cree tres listas listas, una con los menores, otra con los mayores y otra con los iguales a *k*.
	* Crea otra lista lista con aquellos que son múltiplos de *k*.

			lista=[2,4,6,1,3,4,5,7,8]
			k=4
			lmenor=[]
			ligual=[]
			lmayor=[]
			lmultiplo=[]
			for num in lista:
				if num<k:
					lmenor.append(num)
				if num>k:
					lmayor.append(num)
				if num==k:
					ligual.append(num)
				if num%k==0:
					lmultiplo.append(num)
			print lmayor
			print lmenor
			print ligual
			print lmultiplo

4. Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

		lista=['Di', 'buen', 'dia', 'a', 'papa']
		print lista[::-1]

5. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

		palabra=raw_input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=raw_input("Palabra:")		

		buscar=raw_input("Palabra a buscar:")
		print "La he encontrado %d veces"% lista.count(buscar)

6. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

		palabra=raw_input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=raw_input("Palabra:")		

		buscar=raw_input("Palabra a buscar:")
		sustituir=raw_input("Palabra a sustituir:")		

		cont=0
		for cad in lista:
			if cad==buscar:
				lista[cont]=sustituir
			cont=cont+1		

		print lista

7. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

		palabra=raw_input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=raw_input("Palabra:")		

		eliminar=raw_input("Palabra a eliminar:")		

		while eliminar in lista:
			lista.remove(eliminar)		

		print lista

8. Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

		palabra=raw_input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=raw_input("Palabra lista 1:")		

		palabra=raw_input("Palabra lista 2:")
		lista2=[]
		while palabra != " ":
			lista2.append(palabra)
			palabra=raw_input("Palabra lista 2:")		

		for cad in lista2:
			while cad in lista1:
				lista1.remove(cad)		

		print lista1

9. Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

		palabra=raw_input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=raw_input("Palabra lista 1:")		

		lista2=lista1[::-1]
		print lista2

10. Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

		palabra=raw_input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=raw_input("Palabra lista 1:")		

		lista2=[]
		for cad in lista1:
			if not cad in lista2:
				lista2.append(cad)
		lista1=lista2[:]
		print lista1

11. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

    * Lista de palabras que aparecen en las dos listas.
    * Lista de palabras que aparecen en la primera lista, pero no en la segunda.
    * Lista de palabras que aparecen en la segunda lista, pero no en la primera.
    * Lista de palabras que aparecen en ambas listas.

    Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

		palabra=raw_input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=raw_input("Palabra lista 1:")		

		palabra=raw_input("Palabra lista 2:")
		lista2=[]
		while palabra != " ":
			lista2.append(palabra)
			palabra=raw_input("Palabra lista 2:")		

		# Quito los elementos repetidos de lista1		
		listaaux=[]
		for cad in lista1:
			if not cad in listaaux:
				listaaux.append(cad)
		lista1=listaaux[:]
		print lista1		

		# Quito los elementos repetidos de lista2		
		listaaux=[]
		for cad in lista2:
			if not cad in listaaux:
				listaaux.append(cad)
		lista2=listaaux[:]
		print lista2		

		print "Lista de palabras que aparecen en las dos listas."
		lista3=lista1[:]
		lista3.extend(lista2)		

		# Quito los elementos repetidos de lista3
		listaaux=[]
		for cad in lista3:
			if not cad in listaaux:
				listaaux.append(cad)
		lista3=listaaux[:]
		print lista3		

		print "Lista de palabras que aparecen en la primera lista, pero no en la segunda."
		lista4=[]
		for cad in lista1:
			if not cad in lista2:
				lista4.append(cad)
		print lista4
		
		print "Lista de palabras que aparecen en la segunda lista, pero no en la primera."
		lista5=[]
		for cad in lista2:
			if not cad in lista1:
				lista5.append(cad)
		print lista5		

		print "Lista de palabras que aparecen en ambas listas."
		lista6=[]
		for cad in lista1:
			if cad in lista2:
				lista6.append(cad)
		print lista6


12. Escribir una función que reciba una lista de elementos e indique si se encuentran ordenados de menor a mayor o no.

		num=int(raw_input("Número:"))
		lista=[]
		while num>0:
			lista.append(num)
			num=int(raw_input("Número:"))
		lista2=lista[:]
		lista.sort()
		if lista==lista2:
			print "Ordenada"
		else:
			print "No ordenada"

[Volver](index)
