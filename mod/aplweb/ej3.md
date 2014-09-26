---
layout: index

title: Aplicaciones web
tagline: CFGM SMR
---

### Ejercicio 3: xhtml. Formato de texto.

1. Determinar el código HTML correspondiente a la siguiente página (utiliza com plantilla el [modelo de fichero xhtml](http://dit.gonzalonazareno.org/~josedom/xhtml/modelo.txt)):
	
	![ej1](img/ej3_1.png)

2. Estructurar y marcar el siguiente texto extraído de la [Wikipedia](http://es.wikipedia.org/wiki/Exploracion_espacial) para que el navegador lo muestre con el aspecto de la siguiente imagen:

	![ej2](img/ej3_2.png)

3. Estructurar y marcar el siguiente texto para que el navegador lo muestre con el aspecto de la siguiente imagen:

	![ej3](img/ej3_3.png)

4. Determinar el código XHTML que corresponde con el siguiente documento:

	![ej4](img/ej3_4.png)
	
5. Determinar el código XHTML que corresponde al siguiente documento:

	![ej5](img/ej3_5.png)
	
6. Estructurar y marcar el siguiente texto para que el navegador lo muestre con el aspecto de la siguiente imagen:

	![ej6](img/ej3_6.png)

7. Estructurar y marcar el siguiente texto para que el navegador lo muestre con el aspecto de la siguiente imagen:

	![ej7](img/ej3_7.png)
	
8. Vuelve al ejercicio nº 2 de esta relación e incluye en su cabecera (<head>...</head>) la siguiente descripción de estilo, sustituyendo cada comentario por su correspondiente selector:

	**Selector:** indica el elemento o elementos HTML a los que se aplica la regla CSS. Para más [información](http://librosweb.es/css/capitulo_2/selectores_basicos.html).

		<style type="text/css">
			/* Todos los elementos de la pagina */
			{ font: 1em/1.3 Arial,Helvetica, sans-serif; }
			/* El titular de la pagina */
			{ font: 3em/1.3 Garamond,Helvetica, sans-serif; text-align:center;color: #ff0000; }
			/* Los dos primeros parrafos usando la etiqueta "div"*/
			{ border: 2px double #ff0000;padding: 5px; color: #336699; }
			/* Los dos ultimos parrafos usando el atributo "class" */
			{ color:339966; padding-left: 20px; padding-right: 20px;}
			/* Todos los elementos "strong" de los dos primeros parrafos */
			{ background: #ffffcc; padding: .1em; font-weight:bold; }
			/* Todos los elementos "cite" de los dos primeros parrafos */
			{ font-style:italic; }
			/* Todos los elementos "strong" y cite de los dos ultimos parrafos */
			{ text-decoration: underline; }
		</style>

	El aspecto final deberá ser algo parecido a esto:

	![ej8](img/ej3_8.png)
	
9. Haz lo mismo con el ejercicio nº 3, según la siguiente descripción de estilo:

		<style type="text/css">
			/* Todo el cuerpo de la pagina */
			{ font: 14px "Century Gothic","Trebuchet MS",Arial,Helvetica, sans-serif;background:#ffff99; }
			/* El titular de la pagina */
			{ font: 2em/1.3 "Trebuchet MS",Arial,Helvetica, sans-serif;background:#f0f0f0;color: navy;border: 6px inset #ff0000;padding: 10px;}
			/* La referencia a la ciudad de "Washington" en el primer parrafo */
			{ font-size: 1.5em;font-weight:bold; }
			/* Los acronimos */
			{ font-size: 1.2em;text-decoration: underline; }
			/* La cita del final */
			{ font-style: italic;padding-left: 20px;padding-right: 20px;text-align: right;}
		</style>

	El aspecto final deberá ser algo parecido a esto:

	![ej9](img/ej3_9.png)


10.  Crea un documento web que contenga un glosario de términos ordenados alfabéticamente, de los vistos en el tema de Introducción de la asignatura. Cada término deberá tener una breve definición de su significado. Finalmente añádele un formato libre, pero decente, utilizando CSS. Se valorará de forma positiva el uso del máximo número posible de etiquetas vista en este tema. Entrega una captura de pantalla donde se vea el resultado de la validación de la página.

[Volver](index)
