---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Boletín 6: Ejercicios diccionarios, ficheros, ...

1. Realiza el ejercicio 3 y 4 del [boletín 3](http://dit.gonzalonazareno.org/moodle/pluginfile.php/3306/mod_resource/content/1/ejercicios_python3.pdf). Nota: No hace falta hacer la última solución "de fuerza bruta", pero si estas aburrido puedes intentarlo. Puedes encontrar ficheros con contraseñas más usadas en este [repositorio de github](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

2. Utilizando el fichero [notas.csv](notas.csv), realiza un programa en python que lea los datos de ese fichero y construya la siguiente estructura: 

        alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
                    {"nombre":"Rafaela", ... },...]

Crea un programa que te de muestre un menú y puedas elegir una de estas opciones:
    
    * Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para realizar el cálculo de la nota media.
    * Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
    * Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
    * Pide un curso, y crea un fichero *nombredelcurso*.txt con los alumnos y la nota media.

3. Descarga el fichero [zips.json](http://media.mongodb.org/zips.json) del sitio de mongodb. Se trata de un listado de los códigos postales de EEUU en formato JSON (lo que Python denomina diccionarios y listas). Realiza los siguientes ejercicios

    * Cuenta el número de códigos postales que aparecen
    * Cuenta el número de códigos postales de cada estado
    * Obtén la URL del mapa de OpenStreetMap de la ciudad de "Akaska" en el estado de Dakota del Sur (SD). Nota: Las coordenadas que aparecen en el fichero zips.json vienen en formato [longitud,latitud] y la url genérica que utiliza OpenStreetMap es:

            http://www.openstreetmap.org/#map=zoom/latitud/longitud

    Por ejemplo:

    [http://www.openstreetmap.org/#map=19/37.27058/-5.91958](http://www.openstreetmap.org/#map=19/37.27058/-5.91958) para ver con un zoom de nivel 19 la ubicación con latitud 37.27058 y longitud -5.91958



[Volver](index)