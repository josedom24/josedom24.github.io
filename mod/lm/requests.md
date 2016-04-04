---
layout: index

title: Lenguajes de marcas
tagline: CFGS ASIR
---

### Ejercicios libreria requests

Realiza programas en python que utilizando la librería requests, realicen las siguientes acciones.

1. Programa que muestre el nombre de los proyectos públicos de la aplicación redmine de nuestro ciclo. Utiliza la respuesta XML.

2. Programa que muestre el nombre de los proyectos de la aplicación redmine de nuestro ciclo. Para ello necesitas autentificarte con la API key. Utiliza la respuesta XML. 

	Si queremos subir este programa a github, debería buscar algún mecanismo para no guardar nuestra **key** en el repositorio público de github. Tenemos dos soluciones:

	* **Usar un fichero de configuración**:

	Guardamos la key en un fichero de configuración (por ejemplo que llamamos key.cfg) que nunca subimos a github (el nombre de este fichero se guarda en un fichero .gitignore). En nuestro programa podemos utilizar un código de esta forma:

		with open("key.cfg", "r") as archivo: 
    		key = archivo.read() 