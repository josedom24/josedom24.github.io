---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Autentificación básica

El servidor web Apache puede acompañarse de distintos módulos para proporcionar diferentes modelos de autenticación.
La primera forma que veremos es la más simple. Usamos para ello el módulo de autenticación básica que viene instalada “de serie” con cualquier Apache: [mod_auth_basic](http://httpd.apache.org/docs/2.2/es/mod/mod_auth_basic.html). La configuración que tenemos que añadir en el fichero de definición del Virtual Host a proteger podría ser algo así:

        <Directory "/var/www/miweb/privado">
         Order deny,allow
         AuthUserFile "/etc/apache2/claves/passwd.txt"
         AuthName "Palabra de paso"
         AuthType Basic
         Require valid-user
        </Directory>

El método de autentificación básica se indica en la directiva [AuthType](http://httpd.apache.org/docs/2.2/es/mod/core.html#authtype).  

* En Directory escribimos el directorio a proteger, que puede ser el raíz de nuestro Virtual Host o un directorio interior a este. 
* En [AuthUserFile](http://httpd.apache.org/docs/2.2/es/mod/mod_authn_file.html#authuserfile) ponemos el fichero que guardará la información de usuarios y contraseñas que debería de estar, como en este ejemplo, en un directorio que no sea visitable desde nuestro Apache. Ahora comentaremos la forma de generarlo. 
* Por último, en [AuthName](http://httpd.apache.org/docs/2.2/es/mod/core.html#authname) personalizamos el mensaje que aparecerá en la ventana del navegador que nos pedirá la contraseña.
* Para controlar el control de acceso, es decir, que usuarios tienen permiso para obtener el recurso utilizamos las siguientes directivas: [AuthGroupFile](http://httpd.apache.org/docs/2.2/es/mod/mod_authz_groupfile.html#authgroupfile), [Require user](http://httpd.apache.org/docs/2.2/es/mod/core.html#require), [Require group](http://httpd.apache.org/docs/2.2/es/mod/core.html#require).

El fichero de contraseñas se genera mediante la utilidad htpasswd. Su sintaxis es bien sencilla. Para añadir un nuevo usuario al fichero operamos así:

        # htpasswd /etc/apache2/claves/passwd.txt carolina
        New password:
        Re-type new password:
        Adding password for user carolina

Para crear el fichero de contraseñas con la introducción del primer usuario tenemos que añadir la opción -c (create) al comando anterior. Si por error la seguimos usando al incorporar nuevos usuarios borraremos todos los anteriores, así que cuidado con esto. Las contraseñas, como podemos ver a continuación, no se guardan en claro. Lo que se almacena es el resultado de aplicar una [función hash](http://es.wikipedia.org/wiki/Hash).

        josemaria:rOUetcAKYaliE
        carolina:hmO6V4bM8KLdw
        alberto:9RjyKKYK.xyhk

Para denegar el acceso a algún usuario basta con que borremos la línea correspondiente al mismo. No es necesario que le pidamos a Apache que vuelva a leer su configuración (/etc/init.d/apache2 reload) cada vez que hagamos algún cambio en este fichero de contraseñas, pero si lo es después de hacer los cambios en el fichero de definición del Virtual Host.

 La principal ventaja de este método es su sencillez. Sus inconvenientes: lo incómodo de delegar la generación de nuevos usuarios en alguien que no sea un administrador de sistemas o de hacer un front-end para que sea el propio usuario quien cambie su contraseña. Y, por supuesto, que dichas contraseñas viajan en claro a través de la red. Si queremos evitar esto último podemos crear una [instancia Apache con SSL](http://blog.unlugarenelmundo.es/2008/09/23/chuletillas-y-viii-apache-2-con-ssl-en-debian/).

**Cómo funciona este método de autentificación**

Cuando desde el cliente intentamos acceder a una URL que esta controlada por el método de autentificación básico:

1) El servidor manda una respuesta del tipo 401 *HTTP/1.1 401 Authorization Required* con  una cabecera *WWW-Authenticate* al cliente de la forma:

        WWW-Authenticate: Basic realm="Palabra de paso"

2) El navegador del cliente muestra una ventana emergente preguntando por el nombre de usuario y contraseña y cuando se rellena se manda una petición con una cabecera *Authorization*

        Authorization: Basic am9zZTpqb3Nl

En realidad la información que se manda es el nombre de usuario y la contraseña en base 64, que se puede decodificar fácilmente con cualquier [utilidad](http://www.base64decode.org/).

**Ejercicios**

1) Crea cuatro  usuarios de apache: pepe, maria, juan, ana.

2) Crea dos grupos de usuarios: grupo1 (pepe,maria), grupo2 (juan,ana).

3) Crea un directorio llamado privado1 en el host virtual default, que permita el acceso a todos los usuarios.

4) Crea un directorio llamado privado2 en el host virtual default, que permita el acceso sólo a juan y a ana.

5) Crea un directorio llamado privado3 en el host virtual default, que permita el acceso sólo los usuarios del grupo1.

La directiva [satisfy](http://httpd.apache.org/docs/2.2/mod/core.html#satisfy) controla como el se debe comportar el servidor cuando tenemos autorizaciones a nives de host (order, allow, deny) y tenemos autorizaciones de usuarios (require).

6) El directorio privado3 del ejercicio5 haz que sólo sea accesible desde el localhost, y estudia como se comporta la autorización si ponemos:

        satisfy any
        satisfy all

[Volver](index)
