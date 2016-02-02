---
layout: index

title: Implantación de Aplicaciones Web
tagline: CFGS ASIR
---

### Implantación de una aplicación web estática en Github Pages

La forma tradicional de crear un sitio web estático sería de la siguiente forma:

1. Crear las distintas páginas html en el entorno de desarrollo.
2. Podemos añadir alguna funcionalidad añadiendo código javascript, que se ejecutará en el cliente.
3. El entorno de producción necesita sólo un servidor web.
4. El despliegue podemos hacer usando un servidor ftp para subir los ficheros al servidor.

Ventajas de las páginas estáticas:

* Portabilidad, funcionan en cualquier servidor.
* Tiempos de acceso óptimos, tardan muy poco en cargarse.
* Facilitan el posicionamiento.
* Costos de alojamiento menores.
* Mínimos requerimientos técnicos para su operación.

Desventajas de las páginas estáticas:

* Funcionalidad muy limitada
* No se pueden realizar búsquedas en la página.
* El visitante no tiene ninguna posibilidad de seleccionar, ordenar o modificar los contenidos o el diseño de la página a su gusto.
* El administrador web debe acceder al servidor donde está alojada la página para cambiar los contenidos de la página.
* El proceso de actualización es lento, tedioso y esencialmente manual.
* No se accede a bases de datos (esto puede ser también una ventaja)

#### Github Pages

[Github Pages](https://pages.github.com/) es un servicio que te ofrece Github para publicar de una manera muy sencilla páginas web. Disponemos de la opción de generar de forma automática las páginas utilizando una herramienta gráfica, o la creación y modificación de páginas web usando la línea de comandos con el comando [git](http://rogerdudler.github.io/git-guide/index.es.html).

##### Cómo podemos construir nuestras páginas web

La forma más sencilla de construir nuestro sitio es subir a nuestro repositorio todos los ficheros necesarios: ficheros html, hojas de estilos, javascript, imágenes, etc. Si sólo tuviéramos esta opción de edición de páginas no tendríamos grandes ventajas para decidirnos a escoger este servicio de hosting.

Lo que realmente hace esta herramienta una opción muy potente es que Github Pages suporta [Jekyll](https://jekyllrb.com/), herramienta escrita en Ruby que nos permite generar, de una forma muy sencilla, ficheros HTML estáticos. Aunque esta herramienta esta pensada para generar blogs, nosotros vamos a utilizar algunas de sus funcionalidades para crear páginas estáticas convencionales.

##### Usando Jekyll para crear páginas web

La principal característica de Jekylls es la generación de html estático a partir de dos recursos muy simples:

* Plantillas (templates): Ficheros que contienen el esqueleto de las página html que se van a generar. Estos ficheros normalmente se escriben siguiendo la sintaxis de [Liquid](http://wiki.shopify.com/Liquid).
* Ficheros de contenido: Normalmente escritos en sintaxis [Markdown](http://daringfireball.net/projects/markdown/) y que contienen el contenido de la página que se va a generar.

Por lo tanto una vez que tengo definidas mis plantillas, lo único que tengo que hacer es centrarme en  el contenido escribiendo los diferentes de ficheros de contenido.

##### Usando Markdown para escribir el contenido de nuestras páginas

Los distintos contenidos de nuestras páginas serán definidos en ficheros Markdown con extensión md. La [sintaxis de este lenguaje de marcas](https://guides.github.com/features/mastering-markdown/) es muy sencilla y fácilmente convertible a html. Para practicar las distintas opciones puedes usar este [editor online](http://www.ctrlshift.net/project/markdowneditor/).

#### Mi experiencia

Si las cosas que aprendéis las escribís es probable que no se olviden y se entiendan mejor, por lo tanto tenéis más información en el [artículo](http://www.josedomingo.org/pledin/2013/09/publicar-una-pagina-web-en-github-pages/) que escribí cuando aprendí a hacerlo.

<div class='ejercicios' markdown='1'>

Crea un sitio web usando la herramienta github pages, está página te servirá durante el curso para documentar las distintas prácticas que vamos a realizar en el módulo. Tienes que tener en cuenta:

* Puedes crear una página de usuario, del tipo http://**nombre_de_usuario**.github.io o una página de repositorio, en este caso la url sería http://*nombredeusuaio*.github.io/*nombrederepositorio*
* Puedes crear una página utilizando el generador automático de plantillas, o subiendo directamente una plantilla propia.
* Tiene que tener al menos dos páginas: la principal (index.md) y una página que hablé de ti (about.md), y una imagen.

Comenta en la tarea los pasos relevantes.
</div>
