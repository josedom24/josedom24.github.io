---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Instalación del servidor de correo postfix

#### Instalación de Postfix

Vamos a instalar el servidor de correo postfix, con la siguiente instrucción:

        apt-get install postfix
 

El programa de configuración de paquetes de debian (debconf) hará dos preguntas durante la instalación a las que se debe responder de la siguiente manera:

* Configuración del equipo como "Internet site", que significa que no utiliza ningún otro equipo para enviar el correo con SMTP
* Como nombre de correo ponemos iesgn.org

Estas características se incluyen en el fichero de configuración de postfix (/etc/postfix/main.cf),donde no hay que tocar los parámetros por ahora.

Hay que asegurarse que el fichero /etc/mailname tiene el siguiente contenido: *iesgn.org*

 
Si modificamos algún parámetro de postfix habrá que hacer que el demonio que se está ejecutando vuelva a leer el fichero de configuración mediante:

        service postfix reload

#### Pruebas de funcionamiento
Para comprobar que un servidor de correo está funcionando correctamente hay que hacer pruebas de envío y recepción de correo, tanto el envío como la recepción de correo quedará registrada en el fichero /var/log/mail.log, por lo que conviene abrirlo de forma continua en una terminal:

        tail -f /var/log/mail.log
 

Vamos a utilizar un programa de correo en modo texto: el programa mail que se incluye en el paquete bsd-mailx. Un ejemplo de utilización sería:

        # mail usuario
        Subject: Asunto
        Prueba de envío local
        [CTRL-D]
        Cc:

donde se envía un mensaje al usuario "usuario" del propio equipo y [CTRL-D] indica la señal de EOF (End of file) que se le ha mandado para indicar que se ha terminado de escribir el cuerpo del mensaje.

Para comprobar la recepción del mensaje, el usuario "usuario" ejecutara mail, le saldrán la lista de correos recibidos, para acceder a un correo escribimos su número, para salir del programa escribimos 'q'.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

Realiza la instalación del servidor de correo. Suponiendo que tenemos dos usuarios pepe y maría, manda mensajes desde un usuario al otro del servidor.

</div>


[Volver](index)
