---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Mapear URL a ubicaciones de un sistema de ficheros II

1) Crea un host virtual que se llame www.miweb.com cuyo directorio base sea /srv/web.

2) Cuando se entre a la dirección www.miweb.com se redireccionará automaticamente a www.miweb.com/principal, donde se mostrará un mensaje de bienvenida. En el directorio principal no se permite ver la lista de los ficheros, no se permite que se siga los enlaces símbolicos y no se permite negociación de contenido.

3) Debe existir una URL que sea www.miweb.com/principal/miscosas, que visualize el directorio home del usuario. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces símbolicos siempre que sean a ficheros o directorios cuyo dueño sea el usuario.

4) En la URL www.miweb.com/principal/internacional, debe existir dos mensajes de bienvenida: en inglés y en español, por lo tanto se debe permitir la negociación de contenidos. Realiza una prueba de funcionamiento, donde se demuestre que se ha accedido a la web desde un navegador con el español como idioma configurado, y que se accedido con el inglés.

5) En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error.

6) En al url www.miweb.com/images deben a aparecer los ficheros que se encuentran en /usr/share/apache2/icons/

[Volver](index)
