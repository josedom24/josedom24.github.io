---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
# Implantación de un servidor de hosting

#### (9 tareas - 35 puntos)(3 tareas obligatorias - 10 puntos)


El objetivo de la práctica es montar un servidor que ofrezca un servicio de de hospedaje de páginas web con las siguientes características:

* Podemos dar de alta a un usuario y al nombre de dominio (por ejemplo nombrededominio.com) por el que va estar referido su espacio.
* Se podrán hospedar páginas estáticas (html) y páginas web dinámicas construidas con PHP.
* Automáticamente se creará una página principal, que al acceder a la pagina web (www.nombrededominio.com) de la bienvenida e informe que dicha página está en construcción.
* Para gestionar los ficheros hospedados en nuestro espacio utilizaremos un servidor FTP ftp.nombrededominio.com.
* Para gestionar las tablas de mysql accederemos al programa phpmyadmin en la dirección mysql.nombrededominio.com.

<div class='ejercicios' markdown='1'>

* **Tarea 1 (4 puntos)(Obligatorio):** Contesta las siguientes preguntas:

1. ¿Qué servidores necesitas instalar en la máquina donde vamos a implantar el hosting?
Cuando damos de alta una nueva cuenta en nuestro hosting hay que indicar un usuario y un nombre de dominio. ¿Qué acciones hay que hacer en el servidor con el usuario? ¿Qué acciones hay que hacer con el nombre de dominio?
2. ¿Cómo puedes comprobar que existe ya un usuario con el mismo nombre?¿y qué ya está dado de alta un determinado nombre de dominio?
3. ¿Qué debes tener en cuenta, a la hora de crear el directorio home del usuario, para que accediendo por ftp, el usuario pueda gestionar su página web?
4. ¿Cuantos nombres habrá que dar de alta en la zona de resolución directa de nombrededominio.com?
</div>

## Especificaciones técnicas mínimas

* El sistema utilizará usuarios virtuales cuya información estará guardad en una base de datos mysql.
* El administrador debe decidir la estructura para guardar los directorios personales de los usuarios.
Cuando se da de alta un nuevo usuario con un nombre de dominio, habr´a que tener en cuenta las siguientes consideraciones:

1. Si el usuario o el nombre del dominio existen, no se continúa.
2. Se creará el directorio personal del usuario, este directorio será el *DocumentRoot* del servidor web. En este directorio se tendrá que crear una página web de bienvenida.
3. Se creará un nuevo virtual hosting (www.nombrededomino.com) con el DocumentRoot apuntando al directorio personal que anteriormente hemos instalado.
4. Se creará un nuevo usuario virtual para el acceso por FTP. El administrador decidirá la política para generar la contraseña. Dicha contraseña generada tendrá que visualizarse por pantalla. La contraseña será guardada en la base de datos encriptada.
5. Se creará un nuevo usuario en el gestor de base de datos mysql, se debe llamar mynombredeusuario, la contraseña que se genere para mysql debe ser distinta a la generada para la gestión del FTP y también se debe mostrar.
6. Se creará una nueva zona nombrededominio.com en el servidor DNS bind9 con las zonas de resolución directa e inversa que permitan conocer los distintos nombres (www,ftp, mysql, ...)

<div class='ejercicios' markdown='1'>

* **Tarea 2 (3 puntos)(Obligatorio):** Escribe una guía donde se vean los comandos y las modficaciones de configuración que hay que hacer en los servidores, para conseguir cada uno de los puntos anteriormente descritos.

* **Tarea 3 (3 puntos)(Obligatorio):** Escribe una guía donde se vean los comandos y las modficaciones de configuración que hay que hacer para dar de baja a un usuario y el nombre de dominio asociado.


</div>

## Creación de un script

Crea los siguientes scripts:

* Un script bash/python (alta) que reciba el nombre del usuario y el nombre de dominio relacionado con el usuario, y realice los pasos mostrados anteriormente.
* Un script bash/python (baja) que reciba un nombre de dominio e elimine la cuenta del usuario relacionado a dicho nombre de dominio. Borrará el vitual host de apache2, la zona del servidor DNS, el usuario de la base de datos y las bases de datos creados, el usuario virtual para el acceso a la base de datos y el directorio personal del usuario.
* Un script bash/python (change_password) que nos permite cambiar las contraseñas de un determinado usuario. Por lo tanto recibe el nombre de un usuario, una opción (-sql, si queremos cambiar la contraseña de mysql, o -ftp, si queremos cambar la contraseña del ftp) y un nueva contraseña y haga la modificación de la contraseña indicada si el usuario existe.

<div class='ejercicios' markdown='1'>

* **Tarea 4 (10 puntos: scrpt de alta (5 ptos), script de baja (3 puntos), script de cambio de contraseña (2 puntos)):** Entrega la url del repositorio github donde has guardado los scripts. Haz una prueba de funcionamiento al profesor.

</div>

## Configuración de estadísticas Webs

Configura el sistema para que todos los usuarios puedan acceder a las estadísticas de su alojamiento web usando el programa awstats. Tendremos que tener en cuanta que el acceso a esta información no será público, para acceder a ella el usuario se tendrá que autentificar con el nombre de usuario y la contraseña que se han generado para la gestión ftp.

<div class='ejercicios' markdown='1'>

* **Tarea 5 (2 puntos)**: Crea un sistema de estadística con awstats que sea accesible desde la URL: *stats.nombrededominio.com*. Muestraselá al profesor.

</div>

## Utilización de cuotas

<div class='ejercicios' markdown='1'>

* **Tarea 6 (2 puntos)**: Investiga la forma de limitar el espacio que los usuarios tienen a su disposición, por ejemplo que cada usuario tenga un espacio limitado de 100 Mb.

</div>

## Usuarios virtuales con LDAP

<div class='ejercicios' markdown='1'>

* **Tarea 7 (3 puntos)**: Modifica toda la configuración para que los suarios virtuales que estamos usando se guarden en un servidor LDAP.

</div>

## Aplicación web para la gestión del hosting

<div class='ejercicios' markdown='1'>

* **Tarea 8 (4 puntos)**: Crea una palicación web (con cualquier tecnología, por ejemplo bottle o django) que permita gestionar el hosting: dar de alta nuevas cuentas, borrarlas, modificar contraseñas, ...

</div>

## Creación de subdominios

Queremos añadir a nuestro hosting para que podamos dar de alta a nuevos subdominios. Por ejemplo podemos crear el subdominio *web.nombrededominio.com* que será otra página web del usuario.

<div class='ejercicios' markdown='1'>

* **Tarea 9 (4 puntos)**: Crea un script que nos permita gestionar subdominios en nuestro hosting.

</div>
      
[Volver](index)
