---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

## Servidor proxy/cache squid

#### (10 tareas - 25 puntos)(5 tareas obligatorias - 9 puntos)

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
8. Vamos a realizar un script en python/bash que funcione de la siguiente manera:

		filtrar.sh -opciones -tipo contenido

	Siendo -opciones: -a: añadir, -d: borrar; -tipo: -url: expresa una url, -dom: expresa un dominio; contenido la url o el dominio que queremos añadir o borrar de la lista negra.

9. Los navegadores de los clientes deben terner configurado el proxy de manera automática, indicando en la URL el fichero de configuración PAC: wpad.josedomingo.gonzalonazareno.org/wpad.dat, si no se tiene este fichero configurado no se debe tener acceso a internet.

10. En el fichero pac hay que configurar que el acceso al dominio josedomingo.gonzalonazareno.org no pase por el proxy.

11. Por último tendremos instalado un programa para monitorizar el uso del proxy: sarg. Para visualizar la información generada por dicho programa accederemos a una página web llamada proxy.josedomingo,gonzalonazareno.org que sólo será accesible si ponemos el nombre de usuario y la contraseña de los profesores.

12. Realizar el punto 7 y 8 usando el filtro de contenidos dansguardian. Es decir, las listas negras estarán gestionada por dansguardian. Al script filtrar.sh se le añade un nuevo -tipo: -palabra que permite gestionar las lista de palabras prohibidas. Tendrás que pensar que cambios tienes que hacer en el fichero pac.

13. Configura squid para no tener dos usuarios por defectos (profesor y alumno), sino squid se autentifique con el LDAP que tenéis montado. Modifica la estructura del servidor LDAP para que se puedan distinguir los dos roles: usuarios que son profesores y usuarios que sean alumnos.

<div class='ejercicios' markdown='1'>

* **Tarea 1 (1 punto)(Obligatorio)**: Muestra al profesor: Configura de forma manual el proxy, y accede con un usuario incorrecto.
* **Tarea 2 (2 puntos)(Obligatorio)**: Muestra al profesor: Accede como alumno. Intenta bajar un fichero multimedia.
* **Tarea 3 (2 puntos)(Obligatorio)**: Muestra al profesor: Cambia la hora del servidor a las 15:00 de la tarde y comprueba que no hay conexión.
* **Tarea 4 (2 puntos)(Obligatorio)**: Muestra al profesor: Configura el proxy con el fichero wpad, accede como profesor e intenta bajar un fichero zip.
* **Tarea 5 (2 puntos)(Obligatorio)**: Muestra al profesor: Cambia la fecha del servidor e indica un fin de semana y comprueba que no hay conexión.
* **Tarea 6 (3 puntos)**: Muestra al profesor: Filtra el dominio youtube.com con el script que has desarrollado y prueba que realmente no se puede acceder.
* **Tarea 7 (3 puntos)**: Docuemnta la instalción de sarg, y muestra al profesor las estadísticas de accceso al proxy con sarg.
* **Tarea 8 (3 puntos)**: Documenta las pruebas necesarias para comprobar que el acceso a sarg no ha pasado por el proxy. Muestra el contenido del fichero PAC.
* **Tarea 9 (3 puntos)**: Documenta la configuración de Dansguardian, muestra al profesor el funcionamiento.
* **Tarea 10 (4 puntos)**: Documenta la modificación necesaria para squid se autentfique con LDAP.

</div>

[Volver](index)
