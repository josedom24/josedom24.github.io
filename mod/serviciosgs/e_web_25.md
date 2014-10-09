---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Ejercicio: Ejercicio completo del servidor Web(1) (Tiempo estimado: 12 horas)

1. Instala el servidor web Apache2 en una máquina. Modifica la paǵina index.html que viene por defecto y accede a ella desde un navegador.

2. Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

	1. Cada sitio web tendrá nombres distintos.
	2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

	Los dos sitios web tendrán las siguientes características:

	* El nombre de dominio del primero será www.iesgn.org, su directorio base será /srv/www/iesgn y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
	* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será www.departamentosgn.org, y su directorio base será /srv/www/departamentos. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

3. Configura la resolución estática en los clientes y accede a las páginas web.

4. Modifica la configuración del servidor para que la segunda página sólo sea accesible desde el puerto 8080.

5. Cambia la configuración del sitio web www.iesgn.org para que se comporte de la siguiente forma:

	* Cuando se entre a la dirección www.iesgn.org se redireccionará automaticamente a www.iesgn.org/principal, donde se mostrará el mensaje de bienvenida. En el directorio **principal** no se permite ver la lista de los ficheros, no se permite que se siga los enlaces símbolicos y no se permite negociación de contenido.
	* Si accedes a la página www.iesgn.org/principal/documentos se visualizarán los documentos que hay en /srv/doc. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces símbolicos siempre que sean a ficheros o directorios cuyo dueño sea el usuario.
	* En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error.
	* Como el insitituto es bilingüe, en la URL www.iesgn.org/principal/internacional, debe existir dos mensajes de bienvenida: en inglés y en español, por lo tanto se debe permitir la negociación de contenidos. Realiza una prueba de funcionamiento, donde se demuestre que se ha accedido a la web desde un navegador con el español como idioma configurado, y que se accedido con el inglés.

