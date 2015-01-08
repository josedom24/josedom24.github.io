---
layout: index

title: Servicios de red e internat
tagline: CFGS ASIR
---
### Ejercicio: Gestionar un hosting por ftp

Tenemos que desarrollar la página del instituto www.iesgn.org, y queremos que sea gestionada por medio de un ftp. Tendremos las siguientes funcionalidades:

1. Queremos ofrecer una colección de documentos, y lo vamos a hacer mediante http y ftp anónimo, de esta forma se accederá al mismo directorio si accedo a las siguientes URL:

	* http://www.iesgn.org/documentos
	* ftp://ftp.iesgn.org

2. Cada departamento tendrá su página web en la URL www.iesgn.org/nombredeldepartamento, veamos un ejemplo:

	* El departamento de matemáticas tendrá su página en www.iesgn.org/matematicas
	* Se creará un usuario user_matematicas, que tendrá una contraseña, para que accediendo a ftp.iesgn.org, pueda gestionar los ficheros de su página web.

	Determina los cambios que tienes que ir realizando para ir creando el espacio web para cada uno de los departamentos.

3. Instala la aplicación web net2ftp en el servidor por si tenemos problemas de acceso por el puerto 20/21.

4. El uso de usuarios reales del sistema para el acceso FTP puede tener varias desventajas (gestión, seguridad,...). Modifica la configuración del sistema para que se usen usuarios virtuales para el acceso por FTP, cuya información este guardad en una tabla mysql o en un directorio ldap.


[Volver](index)
