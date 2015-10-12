---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Despliegue de una aplicación web desarrollada en PHP en un servidor dedicado (IaaS)

<div class='nota' markdown='1'>

* **Entorno de desarrollo/pruebas**: Máquina local virtual (vagrant)
* **Entrono de producción**: Servidores dedicados, en nuestros instancias en OpenStack
* **Configuración del entorno**: Automático, usando ansible
* **Método de despliegue**: Vamos a intentar automatizar el despliegue para ello podemos usar:
	* Script (bash/python)
	* Sincronizar una rama de un repositorio git
	* Despliegue con herramienta específica: fabric
	* Control de versión de la base de datos: Flyway,  Liquidbase, dbv.php
</div>
<div class='nota' markdown='1'>

Lectura recomendada: [¿Cómo mantengo bajo control las muchas bases de datos que hay en los entornos de desarrollo, pruebas, producción…?](http://www.javiergarzas.com/2014/07/migracion-bases-de-datos.html)

</div>


<div class='ejercicios' markdown='1'>
Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando qué CMS has elegido. Comenta en la tarea redmine los pasos relevantes que vas realizando.
</div>

Esta tarea consiste en desplegar un CMS de tecnología PHP en un infraestructura dedicada, formada por dos servidores dedicados (que serán dos instancias en el cloud): un servidor va a tener instalado el servidor web y el otro el servidor de base de datos. Como hemos indicado que es conveniente no hacer el despliegue directamente en el entorno de producción, configura dos máquinas virtuales (vagrant) lo más parecido al entrono de producción que vamos a tener. Realiza los siguientes pasos:

* Construye con vagrant el entorno de desarrollo/pruebas
* Configura el entorno de desarrollo/pruebas usando la receta ansible que puedes encontrar en el siguiente [repositorio de GitHub](https://github.com/josedom24/automatizacion_iaw) (modifícala para adaptarla a tu entorno)
* Instala la aplicación web en los dos servidores locales
* Realiza una configuración mínima de la aplicación (Cambia la plantilla, crea algún contenido, ...)

<div class='ejercicios' markdown='1'>
En este momento, muestra al profesor la aplicación funcionando en local. **(3 puntos)**
</div>

Vamos a poner en producción nuestra aplicación web, para ello:

* Configura el entorno de producción usando la misma receta ansible, modifícala para adaptarla a tu nuevo entorno.
* Automatiza el método de despliegue, para ello elije entre alguna de las siguientes opciones (o alguna otra que consideres oportuna):
	* Script (bash/python): que nos permita de forma automática copiar los ficheros al entorno de producción y exportar la base de datos.
	* Sincronizar una rama de un repositorio git, entre los dos entornos.
	* Despliegue con herramienta específica: fabric
* Para desplegar la base de datos, utiliza algún software de control de versiones: Flyway,  Liquidbase, dbv.php


<div class='ejercicios' markdown='1'>

* Muestra al profesor la aplicación funcionando en producción. (despliegue automático **4 puntos**, control de versiones de la base de datos **3 puntos**)
* Realiza algún cambio en el CMS en el entorno de desarrollo/prueba, y despliega de nuevo al entorno de producción.
</div>