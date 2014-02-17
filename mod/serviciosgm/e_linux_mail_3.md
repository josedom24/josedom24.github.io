---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Servidor IMAP y webmail

Internet Message Access Protocol, o su acrónimo IMAP, es un protocolo de red de acceso a mensajes electrónicos almacenados en un servidor. Mediante IMAP se puede tener acceso al correo electrónico desde cualquier equipo que tenga una conexión a Internet. IMAP tiene varias ventajas sobre POP, que es el otro protocolo empleado para obtener correo desde un servidor. Por ejemplo, es posible especificar en IMAP carpetas del lado servidor. Por otro lado, es más complejo que POP ya que permite visualizar los mensajes de manera remota y no descargando los mensajes como lo hace POP.

Para instalar el servidor IMAP ejecutamos la siguiente instrucción:

        apt-get install dovecot-imapd

Para acceder a los correos desde cualquier ordenador de nuestra red local, vamos a instalar un webmail, en nuestro caso squirrelmail

        apt-get install squirrelmail

A continuación tenemos que añadir a la configuración de apache2 el nuevos sitio virtual, para ello tenemos que crear un nuevo enlace simbólico dentro de la carpeta sites-enabled, de la siguiente forma:

        cd /etc/apache2/conf.d
        ln -s /etc/squirrelmail/apache.conf correo

Y por último inicializamos el servidor apache.

Ya podemos acceder desde cualquier navegador a la dirección *http://nombre_del_servidor/squirrelmail*, y acceder con los usuarios del sistema.


<div class='ejercicios' markdown='1'>
##### **Ejercicios**


Instala el servidor imap, y el webmail squirrelmail. Realiza envíos de correos electrónicos usando el webmail.

</div>


[Volver](index)
