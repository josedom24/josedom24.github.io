---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
# Proyecto 2: Implantación de un servidor de hosting

El objetivo de la práctica es montar un servidor que ofrezca un servicio de de hospedaje de páginas web con las siguientes características:

* Podemos dar de alta a un usuario y al nombre de dominio (por ejemplo nombrededominio.com) por el que va estar referido su espacio.
* Se podrán hospedar páginas estáticas (html) y páginas web dinámicas construidas con PHP.
* Automáticamente se creará una página principal, que al acceder a la pagina web (www.nombrededominio.com) de la bienvenida e informe que dicha página está en construcción.
* Para gestionar los ficheros hospedados en nuestro espacio utilizaremos un servidor FTP ftp.nombrededominio.com.
* Para gestionar las tablas de mysql accederemos al programa phpmyadmin en la dirección mysql.nombrededominio.com.

## Especificaciones técnicas mínimas

* El sistema utilizará usuarios virtuales cuya información estará guardad en una base de datos mysql.
* El administrador debe decidir la estructura para guardar los directorios personales de los usuarios.
* Se tendrá que implementar un script bash/python (alta) que reciba el nombre del usuario y el nombre de dominio relacionado con el usuario, el script tendrá que realizar las siguientes acciones:

1. Si ya existe el nombre de usuario o el nombre de dominio dará un error y no continuará.
2. Creará el directorio personal para el usuario con un fichero index.html estándar.
3. Creará un nuevo virtual hosting (www.nombrededomino.com) en apache2 con el DocumentRoot apuntando al directorio personal que anteriormente hemos instalado.
4. Se creará un nuevo usuario virtual para el acceso por FTP. El administrador decidirá la política para generar la contraseña. Dicha contraseña generada tendrá que visualizarse por pantalla. La contraseña será guardada en la base de datos encriptada.
5. Se creará un nuevo usuario en el gestor de base de datos mysql, se debe llamar mynombredeusuario, la contraseña que se genere para mysql debe ser distinta a la generada para la gestión del FTP y también se debe mostrar.
6. Se creará una nueva zona nombrededominio.com en el servidor DNS bind9 con las zonas de resolución directa e inversa que permitan conocer los distintos nombres (www,ftp, mysql, ...)

* Se implementará un script bash/python (baja) que reciba un nombre de dominio e elimine la cuenta del usuario relacionado a dicho nombre de dominio. Borrará el vitual host de apache2, la zona del servidor DNS, el usuario de la base de datos y las bases de datos creados, el usuario virtual para el acceso a la base de datos y el directorio personal del usuario.
* Se implementará un script bash/python (change_password) que nos permite cambiar las contraseñas de un determinado usuario. Por lo tanto recibe el nombre de un usuario, una opción (-sql, si queremos cambiar la contraseña de mysql, o -ftp, si queremos cambar la contraseña del ftp) y un nueva contraseña y haga la modificación de la contraseña indicada si el usuario existe.



## MEJORA 1: Configuración de estadísticas Webs (optativa)

Configura el sistema para que todos los usuarios puedan acceder a las estadísticas de su alojamiento web usando el programa awstats. Tendremos que tener en cuanta que el acceso a esta información no será público, para acceder a ella el usuario se tendrá que autentificar con el nombre de usuario y la contraseña que se han generado para la gestión ftp.

## MEJORA 2: Utilización de cuotas (optativa)

Modificar la configuración de proftpd, para que cada usuario tenga un espacio limitado de 100 Mb.

## MEJORA 3: Usuarios virtuales con LDAP (optativa)
Modifica toda la configuración para que los suarios virtuales que estamos usando se guarden en un servidor LDAP.

### Estructura de la memoria a entregar
El manual que debes realizar tendrá al menos los siguientes apartados:

1. Objetivos del trabajo y explicación de lo realizado
2. Instalación y configuración del servidor de los distintos servicios
3. Creación de los scripts
4. Conclusiones
5. Bibliografía, páginas webs de referencia,...

Si se ve oportuno el índice puede cambiar, pero los contenidos anteriores deben aparecer. Se valorará positivamente la ampliación de contenidos.

      
[Volver](index)
