---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de sitios web virtuales usando Apache

El objetivo de esta práctica es la puesta en marcha de dos sitios web utilizando el mismo servidor web apache. Hay que tener en cuenta lo siguiente:

1. Cada sitio web tendra nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Queremos construir en nuestro servidor web apache dos sitios web con las siguientes características:

* El nombre de dominio del primero será **www.iesgn.org**, su directorio base será */var/www/iesgn* y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del insituto Gonzalo Nazareno.

* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será **www.departamentosgn.org**, y su directorio base será */var/www/departamentos*. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

Para conseguir estos dos sitios virtuales debes seguir los siguientes pasos:

1. Los ficheros de configuración de los sitios webs se encuentran en el directorio */etc/apache2/sites-available*, por defecto hay dos ficheros, uno se llama default que es la configuración del sitio web por defecto. Necesitamos tener dos ficheros para realizar la configuración de los dos sitios virtuales, para ello vamos a copiar el fichero default:

        cd /etc/apache2/sites-available
        cp 000-default.conf iesgn.conf
        cp 000-default.conf departamentos.conf

    De esta manera tendremos un fichero llamado *iesgn.conf* para realizar la configuración del sitio web www.iesgn.org, y otro llamado *departamentos.conf* para el sitio web www.departamentosgn.org.

2. Modificamos el fichero *iesgn.conf, donde vamos a añadir la siguiente línea:

        ServerName www.iesgn.org

    Realiza los cambios similares al fichero *departamentos.conf*.

3. No es suficiente crear los ficheros de configuración de cada sitio web, es necesario crear un enlace simbólico a estos ficheros dentro del directorio */etc/apache2/sites-enabled*, para ello:

        a2ensite iesgn
        a2ensite departamentos

    La creación de los elaces simbólicos se puede hacer con la instrucción *a2ensite nombre_fichero_configuracion*, para deshabilitar el sitio tenemos que borrar el enlace simbólico o usar la instrucción *a2dissite nombre_fichero_configuracion*.

4. Crea los directorios y los ficheros index.html necesarios y reiniciamos el servicio:

        systemctl reload apache2

5. Para terminar lo único que tendremos que hacer es cambiar el fichero hosts en los clientes y poner dos nuevas líneas donde se haga la conversión entre los dos nombre de dominio y la dirección IP del servidor.

####Cambiar el *DocumentRoot*

En los VirtualHost que hemos creado el *DocumentRoot* han sido subdirectorios de */var/www*. Para que esto funcione de forma adecuada en el fichero de configuración del servidor web (apache2.conf) podemos encontrar las siguientes líneas:

        <Directory /var/www/>
          Options Indexes FollowSymLinks
          AllowOverride None
          Require all granted
        </Directory>

Si queremos cambiar de directorios y por ejemplo guardar los VirtualHost en el directorio /srv/www, tendremos que cambiar las líneas anteriores y poner los siguiente:

        <Directory /srv/www/>
          Options Indexes FollowSymLinks
          AllowOverride None
          Require all granted
        </Directory>


<div class='ejercicios' markdown='1'>
##### **Ejercicios**

Queremos construir en nuestro servidor web Apache dos sitios web con las siguientes características:

1. El nombre de dominio del primero será *www.iesgn.com*, su directorio base será */var/www/iesgn* y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del insituto Gonzalo Nazareno.
2. En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será *www.departamentosgn.com*, y su directorio base será */var/www/departamentos*. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

Modifica el fichero hosts en los clientes y en el servidor para que se pueda acceder a los sitios web creados.

</div>

[Volver](index)
