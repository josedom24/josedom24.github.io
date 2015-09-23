---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Despliegue de una aplicación web desarrollada en PHP en hosting compartido

<div class='nota' markdown='1'>

* **Entorno de desarrollo/pruebas**: Máquina local virtual (vagrant)
* **Entrono de producción**: Hosting compartido
* **Configuración del entorno**: Manual
* **Método de despliegue**: Tradicional con FTP/SSH
</div>

<div class='ejercicios' markdown='1'>
Antes de empezar con el despliegue de la aplicación web, actualiza esta tarea comentando qué CMS has elegido. Comenta en la tarea redmine los pasos relevantes que vas realizando.
</div>

Esta tarea consiste en desplegar un CMS de tecnología PHP en un hosting compartido, pero es conveniente no hacer el despliegue directamente en el entorno de producción sino que se seguirá el siguiente procedimiento:

* Crea una instancia de vagrant basado en un box debian o ubuntu
* Instala en esa máquina virtual toda la pila LAMP
* Crea una BBDD local para la aplicación web
* Descarga e instala en local la aplicación web
* Realiza una configuración mínima de la aplicación (Cambia la plantilla, crea algún contenido, ...)

<div class='ejercicios' markdown='1'>
En este momento, muestra al profesor la aplicación funcionando en local.
</div>

* Date de alta en un servicio de hosting compartido con soporte para PHP
* Configura adecuadamente todos los parámetros (DNS, usuarios, BBDD, etc.)
* Transfiere los ficheros de la aplicación web desde el entorno de desarrollo utilizando FTP o SSH
* Realiza un volcado de la base de datos local y utilízalo para configurar la base de datos en el entorno de producción
* Verifica el buen funcionamiento de la aplicación en el entorno de hosting compartido

<div class='ejercicios' markdown='1'>

* Muestra al profesor la aplicación funcionando en producción.
* Realiza algún cambio en el CMS en el entorno de desarrollo/prueba, y despliega de nuevo al entorno de producción.
</div>