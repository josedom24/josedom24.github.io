---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

## Servidor proxy/cache squid

#### (8 tareas - 20 puntos)(4 tareas obligatorias - 7 puntos)

Queremos instalar un servidor proxy/cache en nuestro servidor taz. Con ello vamos a poder controlar las páginas web a las que accedamos, además de acelerar nuestra navegación.

Nos piden la configuración de un proxy/cache/filtro en nuestra infraestrucutra. Hemos elegido como proxy/cache squid3, y como filtro de contenido dansguardian. Tenemos que tener en cuenta las siguientes consideraciones:

1. El proxy/cache sólo admite conexiones de la red local.
2. Tenemos dos clases de usuarios: profesores y alumnos.
3. Todos los profesores acceden al proxy con un solo nombre de usuario (profesor) y una única contraseña (pass_profe).
4. Todos los alumnos acceden al proxy con un solo nombre de usuario (alumno) y una única contraseña (pass_alum).
5. Se deniega cualquier conexión que no este autentificada con alguno de estos usuarios.
6. Se quieren limitar las siguientes conexiones:

	* Para los profesores y alumnos:
		* No se pueden bajar ficheros que se puedan instalar (exe,msi,rar,zip,bin,iso).
		* No tienen acceso a internet los fines de semana.	

	* Para los alumnos:
	  	
		* No pueden ver contenido multimedia.
		* Sólo tienen conexión de 8:00 h. a 14:00 h.

7. El control de las páginas permitidas se hará mediante listas negras usando squid.

8. Por último tendremos instalado un programa para monitorizar el uso del proxy: sarg. Para visualizar la información generada por dicho programa accederemos a una página web llamada proxy.josedomingo,gonzalonazareno.org que sólo será accesible si ponemos el nombre de usuario y la contraseña de los profesores.

9. Realizar el punto 7 usando el filtro de contenidos dansguardian. Es decir, las listas negras estarán gestionada por dansguardian. 


<div class='ejercicios' markdown='1'>

* **Tarea 1 (1 punto)(Obligatorio)**: Muestra al profesor: Configura de forma manual el proxy, y accede con un usuario incorrecto.
* **Tarea 2 (2 puntos)(Obligatorio)**: Muestra al profesor: Accede como alumno. Intenta bajar un fichero multimedia.
* **Tarea 3 (2 puntos)(Obligatorio)**: Muestra al profesor: Cambia la hora del servidor a las 15:00 de la tarde y comprueba que no hay conexión.
* **Tarea 4 (2 puntos)(Obligatorio)**: Muestra al profesor: Accede como profesor e intenta bajar un fichero zip.
* **Tarea 5 (2 puntos)**: Muestra al profesor: Cambia la fecha del servidor e indica un fin de semana y comprueba que no hay conexión.
* **Tarea 6 (3 puntos)**: Muestra al profesor: Filtra el dominio youtube.com en la lista negra y prueba que realmente no se puede acceder.
* **Tarea 7 (4 puntos)**: Documenta la instalación de sarg, y muestra al profesor las estadísticas de accceso al proxy con sarg.
* **Tarea 8 (4 puntos)**: Documenta la configuración de Dansguardian, muestra al profesor el funcionamiento.

</div>

[Volver](index)
