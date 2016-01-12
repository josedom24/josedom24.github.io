---
layout: index

title: Servicios de red e internat
tagline: CFGS ASIR
---
### Práctica: Gestionar un hosting por ftp

#### (5 tareas - 15 puntos)(2 tareas obligatorias - 5 puntos)

Tenemos que desarrollar la página del instituto www.iesgn.org, y queremos que sea gestionada por medio de un ftp. Tendremos las siguientes funcionalidades:

* Queremos ofrecer una colección de documentos, y lo vamos a hacer mediante http y ftp anónimo, de esta forma se accederá al mismo directorio si accedo a las siguientes URL:

	* http://www.iesgn.org/documentos
	* ftp://ftp.iesgn.org

<div class='ejercicios' markdown='1'>

* **Tarea 1 (2 puntos)(Obligatorio):** Configura apache2 y el servidor ftp de forma anónimo para obtener el resultado pedido. Entrega la configuración de ambos servidores y muestra al profesor el funcionamiento. 

</div>


* Cada departamento tendrá su página web en la URL www.iesgn.org/nombredeldepartamento, veamos un ejemplo:

	* El departamento de matemáticas tendrá su página en www.iesgn.org/matematicas
	* Se creará un usuario user_matematicas, que tendrá una contraseña, para que accediendo a ftp.iesgn.org, pueda gestionar los ficheros de su página web.

	Determina los cambios que tienes que ir realizando para ir creando el espacio web para cada uno de los departamentos.

<div class='ejercicios' markdown='1'>

* **Tarea 2 (3 puntos)(Obligatorio):** Entrega una pequeña guía que explique las acciones que hay que realizar para crear la página web de un determinado departamento. Muestra al profesor el funcionamiento para la asignatura de "informática".

</div>

* Escribe un pequeño script *crear_pagina_web*, que recibe como parámetro el nombre del departamento y realiza los pasos para crear la página web de departamento y que un usuario accediendo por ftp pueda gestionarla.

<div class='ejercicios' markdown='1'>

* **Tarea 3 (3 puntos):** Entrega la url del repositorio github, y haz una prueba al profesor.

</div>

* Instala la aplicación web net2ftp en el servidor por si tenemos problemas de acceso por el puerto 20/21.

<div class='ejercicios' markdown='1'>

* **Tarea 4 (3 puntos):** Muestra al profesor al acceso a la aplicación web net2ftp.

</div>

* El uso de usuarios reales del sistema para el acceso FTP puede tener varias desventajas (gestión, seguridad,...). Modifica la configuración del sistema para que se usen usuarios virtuales para el acceso por FTP, cuya información este guardada en una tabla mysql o en un directorio ldap.

<div class='ejercicios' markdown='1'>

**Tarea 5 (4 puntos):** Entrega los pasos más relevantes para realizar esta tarea. Y muestra al profesor su funcionamiento.

</div>