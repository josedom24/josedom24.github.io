---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Boletín 8: Ejercicio de ficheros, diccionarios y funciones

Vamos a crear un programa que lea los resultados de los partidos de la liga española en el año 2016-2017, y nos devuelva información sobre estos datos.

El programa leerá la información del siguiente [fichero](liga.csv), que tiene la siguiente estructura: Fecha, Equipo que juega en casa, Equipo que juega fuera, resultado al final del partido y resultado en el intermedio.

El programa ofrecerá un menú, para seleccionar la información deseada:

  1. **Estadística de un equipo**: Nos pide por teclado el nombre de un equipo y nos muestra el número de goles que ha metido, los paridos ganados, perdidos y empatados.
  2. **Nombres de equipos**: Nos muestra la lista de equipos que juegan.
  3. **Clasificación de la liga**: Nos muestra los tres primeros equipos de la liga.
  4. **Quiniela por fecha**: Introducimos una fecha y nos dice los resultados de la quiniela de ese día.
  5. **Salir**

Para realizar este programa podemos realizar las siguientes funciones:

  * menu(): Muestra el menú y devuelve un entero con la opción escogida.
  * LeerPartidos(): Función que lee el fichero y devuelve una lista con los partidos (cada partido se va a guardar en un diccionario).
  * SumarGoles(equipo): Función que recibe un nombre de un equipo y devuelve el total de goles metidos.
  * InfoEquipos(equipo): Función que recibe un nombre de un equipo y devuelve una  lista con los paridos ganados, perdidos y empatados.
  * Equipos(): Función que devuelve una lista con todos los equipos.
  * Quiniela(dia,mes,año): Función que recibe el día, el mes y el año. Y devuelve una lista con los partidos y resultados de la quiniela.
