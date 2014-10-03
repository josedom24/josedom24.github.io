---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Ejercicio: Ejercicio completo del servidor Web(1)

1. Instala el servidor web Apache2 en un servidor. Modifica la paǵina index.html que viene por defecto y accede a ella desde un navegador.

2. Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

	1. Cada sitio web tendrá nombres distintos.
	2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

	Los dos sitios web tendrán las siguientes características:

	* El nombre de dominio del primero será www.iesgn.org, su directorio base será /srv/www/iesgn y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
	* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será www.departamentosgn.org, y su directorio base será /srv/www/departamentos. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

3. Configura la resolución estática en los clientes y accede a las páginas web.

4. Modifica 