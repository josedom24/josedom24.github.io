---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Introducción al Virtual hosting con apache 2.2

Para más información sobre este tema puedes leer: <http://httpd.apache.org/docs/2.2/es/vhosts/>

<div class='nota' markdown='1'>
Desactiva el sitio por defecto y borra la configuración en /etc/apache2/apache2.conf del [ejercicio anterior](e_web_3).
</div>

El objetivo de esta práctica es la puesta en marcha de dos sitios web utilizando el mismo servidor web apache. Hay que tener en cuenta lo siguiente:

1. Cada sitio web tendrá nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Queremos construir en nuestro servidor web apache dos sitios web con las siguientes características:

1. El nombre de dominio del primero será www.iesgn.org, su directorio base será /var/www/iesgn y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
2. En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será www.departamentosgn.org, y su directorio base será /var/www/departamentos. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

Para conseguir estos dos sitios virtuales debes seguir los siguientes pasos:

1.Los ficheros de configuración de los sitios webs se encuentran en el directorio /etc/apache2/sites-available, por defecto hay dos ficheros, uno se llama default que es la configuración del sitio web por defecto. Necesitamos tener dos ficheros para realizar la configuración de los dos sitios virtuales, para ello vamos a copiar el fichero default:

        cd /etc/apache2/sites-available
        cp default iesgn
        cp default departamentos

    De esta manera tendremos un fichero llamado iesgn para realizar la configuración del sitio web *www.iesgn.org*, y otro llamado departamentos para el sitio web *www.departamentosgn.org*.

2.Modificamos el fichero iesgn, donde vamos a añadir la siguiente línea:

        ServerName www.iesgn.org

    Y vamos a modificar dos líneas:

        DocumentRoot /var/www/iesgn/
        .
        .
        .
        <Directory /var/www/iesgn/>
	

    Quedaría un fichero parecido a este:

        <VirtualHost *:80> 
        ServerAdmin admin@ies.org 
        ServerName www.iesgn.org 
        DocumentRoot /var/www/iesgn/ 
        <Directory /> 
           Options FollowSymLinks 
           Allow Override None 
        </Directory> 
        <Directory /var/www/iesgn> 
           Options Indexes FollowSymLinks MultiViews 
           AllowOverride None 
           Order allow,deny 
           allow from all 
        </Directory> 
        ...

    Realiza los cambios similares al dichero departamentos.

3.No es suficiente crear los ficheros de configuración de cada sitio web, es necesario crear un enlace simbólico a estos ficheros dentro del directorio /etc/apache2/sites-enabled, para ello:

        a2ensite iesgn
        a2ensite departamentos

    La creación de los enlaces simbólicos se puede hacer con la instrucción *a2ensite nombre_fichero_configuracion*, para deshabilitar el sitio tenemos que borrar el enlace simbólico o usar la instrucción *a2dissite nombre_fichero_configuracion*

4.Crea los directorios y los ficheros index.html necesarios en /var/www y reiniciamos el servicio:

        service apache2 restart

5.Para terminar lo único que tendremos que hacer es cambiar el fichero hosts en los clientes y poner dos nuevas líneas donde se haga la conversión entre los dos nombre de dominio y la dirección IP del servidor.


[Volver](index)
