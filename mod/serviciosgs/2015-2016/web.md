---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Servidor WEB

#### (18 tareas - 25 puntos)(8 tareas obligatorias - 11 puntos)

<div class='ejercicios' markdown='1'>

* **Tarea 1 (1 punto)(Obligatorio):** Instala el servidor web Apache2 en una máquina. Modifica la paǵina index.html que viene por defecto y accede a ella desde un navegador. Entrega una captura de pantalla accediendo a ella.

</div>

#### Virtual Hosting

Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

1. Cada sitio web tendrá nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Los dos sitios web tendrán las siguientes características:

* El nombre de dominio del primero será www.iesgn.org, su directorio base será /srv/www/iesgn y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será departamentos.iesgn.org, y su directorio base será /srv/www/departamentos. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

<div class='ejercicios' markdown='1'>

* **Tarea 2 (3 punto)(Obligatorio):** Configura la resolución estática en los clientes y muestra al profesor el acceso a cada una de las páginas.

</div>

#### Mapeo de URL

Cambia la configuración del sitio web www.iesgn.org para que se comporte de la siguiente forma:

<div class='ejercicios' markdown='1'>


* **Tarea 3 (1 punto)(Obligatorio):** Cuando se entre a la dirección www.iesgn.org se redireccionará automaticamente a www.iesgn.org/principal, donde se mostrará el mensaje de bienvenida. En el directorio **principal** no se permite ver la lista de los ficheros, no se permite que se siga los enlaces símbolicos y no se permite negociación de contenido. Muestra al profesor el funcionamiento.
* **Tarea 4 (1 punto)(Obligatorio):** Si accedes a la página www.iesgn.org/principal/documentos se visualizarán los documentos que hay en /srv/doc. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces símbolicos siempre que sean a ficheros o directorios cuyo dueño sea el usuario. Muestra al profesor el funcionamiento.
* **Tarea 5 (1 punto):** En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error. Entrega las modificaciones necesarias en la configuración y una comprobación del buen funcionamiento.
* **Tarea 6 (1 punto):** Como el insitituto es bilingüe, en la URL www.iesgn.org/principal/internacional, debe existir dos mensajes de bienvenida: en inglés y en español, por lo tanto se debe permitir la negociación de contenidos. Realiza una prueba de funcionamiento, donde se demuestre que se ha accedido a la web desde un navegador con el español como idioma configurado, y que se accedido con el inglés. Entrega las modificaciones necesarias en la configuración y una comprobación del buen funcionamiento.
</div>

#### Estadísticas web

Vamos a instalar y configurar un analizador de logs de apache2 (webalizer) que nos permita generar estadísticas de acceso a nuestro servidor.

* La URL de la estadística sera *www.masterlan.com/estadistica*.
* El acceso a la estadística desde la red local está permitido, si hace desde fuera, por ejemplo desde el host, se requiere autentificación tipo digest (realizar este punto por medio de un fichero .htaccess)


<div class='ejercicios' markdown='1'>
* **Tarea 7 (2 puntos):** Realiza la instalación de webalizer y muestra al profesor el funcionamiento del mismo teniendo en cuenta los requerimientos señalados.
</div>

#### Autentificación, Autorización, y Control de Acceso

<div class='ejercicios' markdown='1'>
* **Tarea 8 (1 punto)(Obligatorio):** Crea un escenario en Vagrant que tenga un servidor con una red publica, y una privada, un cliente conectada a la red privada. Crea un host virtual que se acceda con el nombre *www.masterlan.com*. A la URL *www.masterlan.com/intranet* sólo se debe tener acceso desde el cliente de la red local, y no se pueda acceder desde la anfitriona por la red pública. A la URL *www.masterlan.com/internet*, sin embargo, sólo se debe tener acceso desde la anfitriona por la red pública, y no desde la red local. Muestra los reultados al profesor.
* **Tarea 9 (1 punto):** Autentificación básica. Limita el acceso a la URL *www.masterlan.com/secreto*. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo se manda la contraseña entre el cliente y el servidor?. Entrega una breve explicación del ejercicio.
* **Tarea 10 (1 punto)(Obligatorio):** Cómo hemos visto la autentificación básica no es segura, modifica la autentificación para que sea del tipo *digest*, y sólo sea accesible a los usuarios pertenecientes al grupo *directivos*. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo funciona esta autentificación? Muestra el funcionamiento al profesor y entrega una breve explicación del ejercicio.
* **Tarea 11 (1 punto):** Vamos a combianar el control de acceso (tarea 8) y la autentificación (tareas 9 y 10), y vamos a configurar el virtual host para que se comporte de la siguiente manera: el acceso a la URL *www.masterlan.com/secreto* se hace forma directa desde la intranet, desde la red pública te pide la autentificación. Muestra el resultado al profesor.
* **Tarea 12 (2 punto):** Utilizando el módulo **libapache2-mod-auth-pgsql**, configura un sitio virtual cuyo acceso sea autentificado mediante usuarios guardados en una base de datos postgreSQL.  Docuementa la tarea.

</div>

#### Configuración con .htaccess
Date de alta en CDMON y contrata una *Plataforma de prueba*. Con ello tenemos a nuestra disposición un hosting comercial con todas sus funcionalidades, incluso con un servidor DNS que nos da acceso al hosting, en mi caso con la URL *http://jdmr.com.mialias.net*. ¿Si necesitamos configurar el servidor web que han configurado los administradores de CDMON que podemos hacer? Explica la directiva **AllowOverride** de apache2. Utilizando archivos .htaccess, y siguiendo esta [guía de CDMON](https://support.cdmon.com/entries/24118027-Informaci%C3%B3n-y-usos-del-fichero-htaccess) realiza las siguientes configuraciones:

<div class='ejercicios' markdown='1'>
* **Tarea 13 (1 punto)(Obligatorio):** Habilita el listado de ficheros en la URL  *http://tunombre.mialias.net/nas*.
* **Tarea 14 (1 punto):** Crea una redirección permanente: cuando entremos en *http://tunombre.mialias.net/google* salte a www.google.es.
* **Tarea 15 (1 punto):** Pedir autentificación para entrar en la URL *http://tunombre.mialias.net/prohibido*. Puedes ver este [tutorial](https://support.cdmon.com/entries/42871258-Proteger-carpetas) de CDMON.

</div>

#### Módulos

<div class='ejercicios' markdown='1'>
* **Tarea 16 (2 puntos)(Obligatorio):** Módulo *userdir*: Activa y configura el módulo *userdir*, que permite que cada usuario del sistema tenga la posibilidad de tener un directorio (por defecto se llama public_html) donde alojar su página web. Publica una página de un usuario, y accede a la misma.
* **Tarea 17 (2 puntos):** Instalación de un servidor WebDAV que sea accesible desde la URL *www.masterlan.com/webdav*.
* **Tarea 18 (2 puntos):** Vamos a volver a nuestro hosting en CDMON, vamos a crear una carpeta php donde vamos a tener un fichero index.php con el siguiente contenido:

		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Conversor de Monedas</title>
		</head>		

		<body>
		<form action="index.php" method="get">
		   	<input type="text" size="30" name="monto" /><br/>
			<select name="pais">
				<option name="Dolar">Dolar</option>
				<option name="Libra">Libra</option>
				<option name="Yen">Yen</option>
			</select>
		    <input type="submit" value="convertir" />
		   </form>
		<?php        
			// averiguamos si se ingresó un motno
			if (isset($_GET['monto'])) {
			  define ("cantidad", $_GET['monto']);
			} else {
		 	  define ("cantidad", 0);
			}
			if($_GET){
			// definimos los paises
			$tasacambios = array ("Libra"=>0.86,"Dolar"=>1.34,"Yen"=>103.56);
			// imprimimos el monto ingresado
			echo "<b>".cantidad." euros</b><br/> ".$_GET["pais"]." = ".cantidad*$tasacambios[$_GET["pais"]]." <br><br>";                                                
			// por cada pais imprimimos el cambio
			}
		   ?> 
		   
		</body>
		</html>

	Prueba la página utilizando parámetros en la URL (parámetros GET), por ejemplo: http://*nombre_página*/php/index.php?monto=100&pais=Libra

	Configura mediante un fichero .htaccess, la posibilidad de acceder a la URL http://*nombre_página*/php/*moneda/cantidad*, donde moneda indica el nombre de la moneda a la que queremos convertir (Dolar,Libra,Yen) y cantidad indica los euros que queremos convertir.

	[Volver](index)
