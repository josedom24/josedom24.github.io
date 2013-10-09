---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Configuración de sitios web virtuales usando IIS


El objetivo de esta práctica es la puesta en marcha de dos sitios web utilizando el mismo servidor web IIS. Hay que tener en cuenta lo siguiente:

* Cada sitio web tendra nombres distintos.
* Cada sitio web compartiran la misma dirección IP y el mismo puerto (80).

Para ello vamos a configurar el servidor web IIS para crear dos nuevos sitios web (**el sitio web predeterminado lo debemos detener**).

Para terminar lo único que tendremos que hacer es cambiar el fichero hosts en los clientes y poner dos nuevas líneas donde se haga la conversión entre los dos nombre de dominio y la dirección IP del servidor.

<div class='ejercicios' markdown='1'>
##### **Ejercicios**

Queremos construir en nuestro servidor web IIS dos sitios web con las siguientes características:

1. El nombre de dominio del primero será *www.iesgn.com*, su directorio base será *c:/inetpub/ies* y contendrá una página llamada index.html, donde sólo se verá una bienvenida a la página del insituto Gonzalo Nazareno.
2. En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será *www.departamentosgn.com*, y su directorio base será *c:/inetpub/departamentos*. En este sitio sólo tendremos una página inicial index.html, dando la bienvenida a la página de los departamentos del instituto.

Modifica el fichero hosts en los clientes y en el servidor para que se pueda acceder a los sitios web creados.

</div>

[Volver](index)
