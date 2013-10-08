---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Hacer peticiones: GET, HEAD y POST
1. Utilizando el comando de linux HEAD visualiza la información de la cabeceras de los siguientes servidores webs:

        http://dit.gonzalonazareno.org
        http://dit.gonzalonazareno.org/~josedom
        http://dit.gonzalonazareno.org/~josedom/xhtml/modelo.txt
        http://dit.gonzalonazareno.org/~josedom/xhtml/linux.jpg

    Identifica todos los parámetros que puedas.

2. Utilizando el método GET obtén el contenido de la página: 

        http://dit.gonzalonazareno.org/moodle/index.php
        http://dit http://www.debian.org/index.html

3. Envío de información al servidor, comprueba como se manda información al servidor mediante el método GET en la URL:

        http://dit.gonzalonazareno.org/~josedom/ejemplo/ejget.php?valor=hola
        http://dit.gonzalonazareno.org/moodle/course/view.php?id=4

    Usando el comando GET manda tu nombre a la página 

        http:/dit.gonzalonazareno.org/~josedom/ejemplo/ejget.php
        
    Usando el comando POST (que envia el contenido en el cuerpo) manda tu nombre a la página 

        http://dit.gonzalonazareno.org/~josedom/ejemplo/ejpost.php

[Volver](index)
