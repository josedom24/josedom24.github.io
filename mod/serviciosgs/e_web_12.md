---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Autentificación tipo digest

La autentificación tipo digest soluciona el problema de la transferencia de contraseñas en claro sin necesidad de usar SSL.  El procedimiento, como veréis, es muy similar al tipo básico pero cambiando algunas de las directivas y usando la utilidad htdigest en lugar de htpassword para crear el fichero de contraseñas. El módulo de autenticación necesario suele venir con Apache pero no habilitado por defecto. Para activarlo usamos la utilidad a2enmod y, a continuación reiniciamos el servidor Apache:

        $ a2enmod auth_digest
        $ /etc/init.d/apache2 restart

Luego incluimos una sección como esta en el fichero de configuración de nuestro Virtual Host:

       <Directory "/var/www/miweb/privado">
         Order deny,allow
         AuthType Digest
         AuthName "dominio"
         AuthUserFile "/etc/claves/digest.txt"
         Require valid-user
       </Directory>

Como vemos, es muy similar a la configuración necesaria en la autenticación básica. Sólo dos notas: el fichero donde se dejan las contraseñas se indicaba con la directiva AuthDigestFile hasta la versión 2.2 de apache. Ahora, como veis en el ejemplo, es AuthUserFile. Y dos: la directiva AuthName que en la autenticación básica se usaba para mostrar un mensaje en la ventana que pide el usuario y contraseña, ahora se usa también para identificar un nombre de dominio (realm) que debe de coincidir con el que aparezca después en el fichero de contraseñas. Dicho esto, vamos a generar dicho fichero con la utilidad htdigest:

        # htdigest -c /etc/claves/digest.txt dominio josemaria
        Adding password for josemaria in realm dominio.
        New password:
        Re-type new password:

Al igual que ocurría con htpassword, la opción -c (create) sólo debemos de usarla al crear el fichero con el primer usuario. Luego añadiremos los restantes usuarios prescindiendo de ella. A continuación vemos el fichero que se genera después de añadir un segundo usuario:

        josemaria:dominio:8d6af4e11e38ee8b51bb775895e11e0f
        gemma:dominio:dbd98f4294e2a49f62a486ec070b9b8c

**Cómo funciona este método de autentificación**

Cuando desde el cliente intentamos acceder a una URL que esta controlada por el método de autentificación de tipo digest:

1) El servidor manda una respuesta del tipo 401 *HTTP/1.1 401 Authorization Required* con  una cabecera *WWW-Authenticate* al cliente de la forma:

        WWW-Authenticate: Digest realm="dominio", 
                          nonce="cIIDldTpBAA=9b0ce6b8eff03f5ef8b59da45a1ddfca0bc0c485", 
                          algorithm=MD5, 
                          qop="auth"

2) El navegador del cliente muestra una ventana emergente preguntando por el nombre de usuario y contraseña y cuando se rellena se manda una petición con una cabecera *Authorization*

        Authorization	Digest username="jose", 
                        realm="dominio", 
                        nonce="cIIDldTpBAA=9b0ce6b8eff03f5ef8b59da45a1ddfca0bc0c485",
                        uri="/digest/", 
                        algorithm=MD5, 
                        response="814bc0d6644fa1202650e2c404460a21", 
                        qop=auth, 
                        nc=00000001, 
                        cnonce="3da69c14300e446b"

La información que se manda es *responde* que en este caso esta cifrada usando md5 y que se calcula de la siguiente manera:

* Se calcula el md5 del nombre de usuario, del dominio (realm) y la contraseña, la llamamos HA1.
* Se calcula el md5 del método de la petición (por ejemplo GET) y de la uri a la que estamos accediendo, la llamamos HA2.
* El reultado que se manda es el md5 de HA1, un número aleatorio (nonce), el contador de peticiones (nc), el qop y el HA2.

Una vez que lo recibe el servidor, puede hacer la misma operación y comprobar si la información que se ha enviado es válida, con lo que se permitiría el acceso.
 

**Ejercicio:**

1) Crea dos subdirectorios en el host virtual defaul que se llamen grupo1 y grupo2. Crea varios usuarios con la utilidad htdigest, asignando a cada uno un dominio distinto (domgrupo1 y domgrupo2). Configura los directorios para que al primero grupo1 sólo puedan acceder los usuarios del dominio domgrupo1, y el directorio grupo2 solo accedan los usuarios del dominio domgrupo2.

[Volver](index)
