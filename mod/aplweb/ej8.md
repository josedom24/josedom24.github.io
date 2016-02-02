---
layout: index

title: Aplicaciones web
tagline: CFGM SMR
---

### Ejercicio 8: css. Selectores, unidades de medidas y colores.

#### Resumen

* **Selector**: indica el elemento o elementos HTML a los que se aplica la regla CSS. Para más [información](http://librosweb.es/css/capitulo_2/selectores_basicos.html).

	* Selector universal: Se utiliza para seleccionar todos los elementos de la página. *
	* Selector tipo etiqueta: Selecciona todos los elementos de la página cuya etiqueta HTML coincide con el valor del selector. Ejemplo: p { }
	* Selector descendente: Selecciona los elementos que se encuentran dentro de otros elementos. Ejemplo: p span
    * Selector de clase: Selecciona todos los elementos que tenga un atributo class determinado. Ejemplo: .destacado, p.destacado
	* Selectores de ID: Selecciona todos los elementos que tenga un atributo id determinado. Ejemplo: #destacado, p#destacado

* **Herencia de estilos**: Cuando se establece el valor de una propiedad CSS en un elemento, sus elementos descendientes heredan de forma automática el valor de esa propiedad. 

* **Unidades de medida**: Las medidas en CSS se emplean, entre otras, para definir la altura, anchura y márgenes de los elementos y para establecer el tamaño de letra del texto.

	* Unidades absolutas: su valor no depende de otro valor de referencia.

    1. in, pulgadas ("inches", en inglés). Una pulgada equivale a 2.54 centímetros.
    2. cm, centímetros.
    3. mm, milímetros.
    4. pt, puntos. Un punto equivale a 1 pulgada/72, es decir, unos 0.35 milímetros.
    5. pc, picas. Una pica equivale a 12 puntos, es decir, unos 4.23 milímetros.

    * Unidades relativas: no están completamente definidas, ya que su valor siempre está referenciado respecto a otro valor.


    1. em, (no confundir con la etiqueta <em> de HTML) relativa respecto del tamaño de letra del elemento. Si se utiliza una tipografía de 12 puntos, 1em equivale a 12 puntos.
    2. ex, relativa respecto de la altura de la letra x ("equis minúscula") del tipo y tamaño de letra del elemento.  El valor de 1ex se puede aproximar por 0.5 em.
    3. px, (píxel) relativa respecto de la resolución de la pantalla del dispositivo en el que se visualiza la página HTML.

    * Porcentajes: Un porcentaje está formado por un valor numérico seguido del símbolo % y siempre está referenciado a otra medida. 

* **Colores**

	* Palabras claves: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, orange, purple, red, silver, teal, white, yellow
    * RGB decimal: rgb(71, 98, 176);
    * RGB porcentual: rgb(27%, 38%, 69%);
    * RGB hexadecimal: #4762B0

#### Ejercicios 

1. A partir del código HTML y CSS que se muestra, añadir los selectores CSS que faltan para aplicar los estilos deseados. Cada regla CSS incluye un comentario en el que se explica los elementos a los que debe aplicarse:
      
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <title>Ejercicio de selectores</title>
        <style type="text/css">
        /* Todos los elementos de la pagina */
        { font: 1em/1.3 Arial, Helvetica, sans-serif; }
         
        /* Todos los parrafos de la pagina */
        { color: #555; }
         
        /* Todos los párrafos contenidos en #primero */
        { color: #336699; }
         
        /* Todos los enlaces la pagina */
        { color: #CC3300; }
         
        /* Los elementos "em" contenidos en #primero */
        { background: #FFFFCC; padding: .1em; }
         
        /* Todos los elementos "em" de clase "especial" en toda la pagina */
        { background: #FFCC99; border: 1px solid #FF9900; padding: .1em; }
         
        /* Elementos "span" contenidos en .normal */
        { font-weight: bold; }
         
        </style>
        </head>
         
        <body>
         
        <div id="primero">
        <p>Lorem ipsum dolor sit amet, <a href="#">consectetuer adipiscing elit</a>. Praesent blandit nibh at felis. Sed nec diam in dolor vestibulum aliquet. Duis ullamcorper, nisi non facilisis molestie, <em>lorem sem aliquam nulla</em>, id lacinia velit mi vestibulum enim.</p>
         
        </div>
         
        <div class="normal">
        <p>Phasellus eu velit sed lorem sodales egestas. Ut feugiat. <span><a href="#">Donec porttitor</a>, magna eu varius luctus,</span> metus massa tristique massa, in imperdiet est velit vel magna. Phasellus erat. Duis risus. <a href="#">Maecenas dictum</a>, nibh vitae pellentesque auctor, tellus velit consectetuer tellus, tempor pretium felis tellus at metus.</p>
         
        <p>Cum sociis natoque <em class="especial">penatibus et magnis</em> dis parturient montes, nascetur ridiculus mus. Proin aliquam convallis ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc aliquet. Sed eu metus. Duis justo.</p>
         
        <p>Donec facilisis blandit velit. Vestibulum nisi. Proin volutpat, <em class="especial">enim id iaculis congue</em>, orci justo ultrices tortor, <a href="#">quis lacinia eros libero in eros</a>. Sed malesuada dui vel quam. Integer at eros.</p>
        </div>
         
        </body>
        </html>     

2. A partir del código HTML proporcionado, añadir las reglas CSS necesarias para que la página resultante tenga el mismo aspecto que el de la siguiente imagen:

    ![ej8](img/ej8_1.png)

    A continuación se muestra el código HTML de la página sin estilos:

        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Ejercicio de selectores</title>
        </head>
         
        <body>
        <h1 id="titulo">Lorem ipsum dolor sit amet</h1>
         
        <p>Nulla pretium. Sed tempus nunc vitae neque. <strong>Suspendisse gravida</strong>, metus a scelerisque sollicitudin, lacus velit 
        ultricies nisl, nonummy tempus neque diam quis felis. <span class="destacado">Etiam sagittis tortor</span> sed arcu sagittis tristique.</p>
         
        <h2 id="subtitulo">Aliquam tincidunt, sem eget volutpat porta</h2>
         
        <p>Vivamus velit dui, placerat vel, feugiat in, ornare et, urna.  <a href="#">Aenean turpis metus, <em>aliquam non</em>, tristique in</a>, pretium varius, sapien. Proin vitae nisi.  Suspendisse <span class="especial">porttitor purus ac elit</span>. Suspendisse eleifend odio at dui. In in elit sed metus pretium elementum.</p>
         
        <table summary="Descripción de la tabla y su contenido">
        <caption>Título de la tabla</caption>
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col" class="especial">Título columna 1</th>
            <th scope="col" class="especial">Título columna 2</th>
          </tr>
        </thead>
         
        <tfoot>
          <tr>
            <th scope="col"></th>
            <th scope="col">Título columna 1</th>
            <th scope="col">Título columna 2</th>
          </tr>
        </tfoot>
         
        <tbody>
          <tr>
            <th scope="row" class="especial">Título fila 1</th>
            <td>Donec purus ipsum</td>
            <td>Curabitur <em>blandit</em></td>
          </tr>
          <tr>
            <th scope="row">Título fila 2</th>
            <td>Donec <strong>purus ipsum</strong></td>
            <td>Curabitur blandit</td>
          </tr>
        </tbody>
        </table>
         
        <div id="adicional">
        <p>Donec purus ipsum, posuere id, venenatis at, <span>placerat ac, lorem</span>. Curabitur blandit, eros sed gravida aliquet, risus justo 
        porta lorem, ut mollis lectus tortor in orci. Pellentesque nec augue.</p>
         
        <p>Fusce nec felis eu diam pretium adipiscing. <span id="especial">Nunc elit elit, vehicula vulputate</span>, venenatis in, 
        posuere id, lorem. Etiam sagittis, tellus in ultrices accumsan, diam nisi feugiat ante, eu congue magna mi non nisl.</p>
         
        <p>Vivamus ultrices aliquet augue. <a href="#">Donec arcu pede, pretium vitae</a>, rutrum aliquet, tincidunt blandit, pede. 
        Aliquam in nisi. Suspendisse volutpat. Nulla facilisi. Ut ullamcorper nisi quis mi.</p>
        </div>
         
        </body>
        </html>

    Aunque la propiedad que modifica el color del texto se explica detalladamente en los próximos capítulos, en este ejercicio solamente es preciso conocer que la propiedad se llama color y que como valor se puede indicar directamente el nombre del color.

    Los nombres de los colores también están estandarizados y se corresponden con el nombre en inglés de cada color. En este ejercicio, se deben utilizar los colores: teal, red, blue, orange, purple, olive, fuchsia y green.

[Volver](index)


