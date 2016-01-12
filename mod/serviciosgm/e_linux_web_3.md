---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Acceso autentificado al servidor web Apache

Otra interesante opción que podemos habilitar en las páginas web de nuestro centro, es la creación de contenidos que sólo puedan ser accedidos vía web mediante el navegador, previa validación del usuario que desea acceder a dichos contenidos, de modo que si el usuario que se autentica está habilitado para ello, accederá a visualizar los contenidos indicados, y en caso contrario no.

Para ello vamos a tener en nuestro directorio base del sitio web una carpeta (que podemos llamar privado) que para acceder a ella será necesario una autentificación.

En el directorio de trabajo de **www.iesgn.org** (*/var/www/iesgn*) vamos a crear una carpeta llamada "profesores" y vamos a hacer que el acceso a esta carpeta necesite autentificación. Dentro de esta carpeta crea un archivo index.html con un mensaje de bienvenida a la zona privada de los profesores.

Para ello hay que seguir los siguientes pasos:

1. En el fichero de configuración de la página www.iesgn.org, /etc/apache2/sites-available/iesgn crea las siguientes líneas:

        <Directory /var/www/iesgn/profesores/>
        	AuthType basic
        	AuthName "Página privada salo para profesores"
        	AuthUserFile /etc/apache2/password
        	Require user pepe
        </Directory>

	Esto quiere decir que para acceder al directorio /var/www/iesgn/profesores/ se necesita autentificación. 

	* El **AuthName** es el mensaje que se va a presentar al usuario
	* El fichero */etc/apache2/password* contiene la contraseña.
	* El usuario permitido se llama pepe. Si ponemos *require valid-user* estaremos indicando que todos los usuario que definamos serán válidos.

	Reiniciamos el servidor apache.

2. Tenemos que crear el fichero de contraseña para los usuarios que tienen permiso. Para ello:

        cd /etc/apache2
        htpasswd -c password pepe

	Esta instrucción pide la contraseña para el usuario pepe y la guarda en el fichero password, la opción -c crea el fichero.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

Vamos a trabajar con los sitios webs de la práctica anterior, debes realizar los siguientes pasos:

1. Crea tres usuarios: director, profesor, alumno.
2. La página www.iesgn.org se puede acceder libremente.
3. La página www.iesgn.org/privado (donde hay una página que da la bienvenida a la zona privada), necesita autentificación y los tres usuarios pueden acceder.
4. La página www.departamentosgn.org necesita autentificación y sólo puede acceder el directo y el profesor.
5. La página www.departamentosgn.org/equipodirectivo, necesita autentificación y sólo el director puede entrar.

</div>

[Volver](index)
