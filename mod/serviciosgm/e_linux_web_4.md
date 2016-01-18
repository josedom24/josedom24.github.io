---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación de un sistema LAMP

El acrónimo 'LAMP' se refiere a un conjunto de subsistemas de software necesarios para alcanzar una solución global, en este caso configurar sitios web o servidores dinámicos con un esfuerzo reducido.

En las tecnologías LAMP esto se consigue mediante la unión de las siguientes tecnologías:

* [Linux](http://es.wikipedia.org/wiki/Linux), el [sistema operativo](http://es.wikipedia.org/wiki/Sistema_operativo);
* [Apache](http://es.wikipedia.org/wiki/Servidor_HTTP_Apache), el [servidor web](http://es.wikipedia.org/wiki/Servidor_web);
* [MySQL](http://es.wikipedia.org/wiki/MySQL), el [gestor de bases de datos](http://es.wikipedia.org/wiki/Gestor_de_bases_de_datos);
* [Perl](http://es.wikipedia.org/wiki/Perl), [PHP](http://es.wikipedia.org/wiki/PHP), o [Python](http://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_Python), los [lenguajes de programación](http://es.wikipedia.org/wiki/Lenguajes_de_programaci%C3%B3n).


Ahora vamos a instalar los paquetes necesarios para tener un entorno LAMP.

#### Apache

        apt-get install apache2

#### MySQL

        apt-get install mysql-server

Durante la instalación del servicio se nos pedirá la contraseña del usuario root del servidor mysql.

* Para acceder al servidor mysql:

        mysql -u root -p

* Muestra las bases de datos:
        
        mysql>show databases; 

* Usamos la base de datos indicadas:

        mysql>use nombre_base_datos; 

* Muestra las tablas de esa base de datos:

        mysql>show tables; 

* Muestra los campos de la tabla indicada:

        mysql>desc nombre_tabla; 

* Muestra los registras de la tabla indicada:

        mysql>select * from nombre_tabla; 

* Crea una base de datos con el nombre indicado:

        mysql>create database nombre_base_datos;

* Crea un usuario con el nombre indicado:

        mysql>create user usuario; 
 
* Da permiso a usuario con la contraseña indicada, para que maneje la base de datos indicada:

        mysql>GRANT ALL ON nombre_base_datos.* TO usuario IDENTIFIED BY 'contraseña_usuario'; 

#### PHP5

        apt-get install php5 libapache2-mod-php5 php5-mysql

Para probar el funcionamiento de Apache y PHP es habitual crear un documento index.php en el directorio /var/www/html con el siguiente contenido:

        <html>
        <body>
        	<? echo phpinfo(); ?>
        </body>
        </html>

Accede desde el navegador del cliente a *http://www.iesgn.org/index.php*

### Instalación de un CMS simple:

Vamos a instalar un CMS muy simple llamado "CMS made simple", para ello sigue estos pasos:

1. [Bájate la versión de la aplicación web:](http://informatica.gonzalonazareno.org/plataforma/file.php/31/cmsmadesimple-1.9.2-base.tar.gz), descomprímelo y guárdalo en una carpeta llamada portal dentro de */var/www/html/portal* (por lo tanto tendremos que acceder a *www.iesgn.org/portal*)

2. Para realizar la instalación accede a *http://www.iesgn.org/portal/install/*.

3. Para que funcione correctamente tenemos que cambiar los permisos a los siguientes directorios:

        cd /var/www/html/portal
        chmod 777 tmp/templates_c; \
        chmod 777 tmp/cache; \
        chmod 777 uploads; \
        chmod 777 uploads/images
        chmod 777 modules

4. Crear el archivo config.php, para eso teclea:

        touch config.php
        chmod 666 config.php

5. Crea una base de datos vacía, y un usuario en la base de datos con los privilegios sobre la base de datos creada,  para ello vamos a hacer los siguiente:

        mysql -u root -p 
        mysql> create database cms;
        mysql>create user user_cms;
        mysql>GRANT ALL ON cms.* TO user_cms IDENTIFIED BY 'asdasd';


6. Vamos a instalar el idioma español, para ello [bájate este fichero](http://s3.amazonaws.com/cmsms/downloads/12788/cmsmadesimple-1.12.1-langpack-es_ES.tar.gz), descomprímelo y copia su contenido dentro de /var/www/html/portal

7. Antes de continuar vamos a instalar una librería gráfica necesaria para el funcionamiento de la páginas:

        apt-get install php5-gd
        /etc/init.d/apache2 restart

8. Una vez realizado todos los cambios, actualiza la página y si todo está bien, podrás escoger el idioma de la página, escoge ES_es.

9. Ahora tenemos 7 pasos para la instalación, en el primero le damos a continuar.

10. El siguiente paso hace las comprobaciones del sistema, si todo es correcto podemos continuar.

11. En el paso 3, nos pide los permiso de creación de fichero, le damos a continuar.

12. En el siguiente paso nos pide los datos del administrador de la página.

13. En al siguiente pantalla, ponemos el nombre de la página y los datos del usuario (user_cms) y la contraseña que tiene (asdasd).

14. En el siguiente paso le damos a continuar y en el siguiente le damos al botón "Ir al panel administrativo".

15. Para acceder a la página entramos en www.iesgn.org/portal, para acceder a la zona administrativa: www.iesgn.org/portal/admin/index.php

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

1. Instala el CMS, entra en la configuración y cambia el nombre del portal.

</div>

[Volver](index)
