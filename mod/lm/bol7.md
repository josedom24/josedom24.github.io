---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Boletín 7: Ejercicios funciones

Necesitamos que se facture el uso de un teléfono. Nos informarán de la tarifa por segundo (en centimos), cuántas comunicaciones se realizaron, la duración de cada comunicación expresada en horas, minutos y segundos. Como resultado deberemos informar la duración en segundos de cada comunicación y su costo.

Vamos a dividir este problemas en problemas más pequeños:

* Cada comunicación se expresa en horas, minútos y segundos, la tarifa es € por segundos, por lo tanto lo primero que vamos a solucionar es convertir las horas, minútos y segundos en segundos. Para ello vamos acrear una función llamada **pasar_a_segundos**. Piensa los parámetros de entrada que tiene esta función y el valor que devuelve. ¿De qué tipo son?
* Una vez que sabemos los segundos que ha tardado una comunicación y la tarifa por segundos vamos a crear una función llamada **calcular_coste** que nos calcule cuanto cuesta, en centimos, la llamada. Piensa los parámetros y el valor devuleto de la función.
* Por último vamos a crear una función para convertir el coste en centimos, en una cantidad de dinero expresda en euros y centimos. Para ello creamos la función **convertir_a_euros**. Piensa los parametros de entrada y los valores devueltos.

**Ejercicios**

1. Crea un programa que te pregunte por teclado la tarifa por segundos en centimos, el número de comunicaciones que se han realizado, y te vaya piediendo horas, minutos y segundo que han durado cada una de las comunicaciones. Finalmente te mostrará cuanto ha costado cada una de las comunicaciones y el total de dinero de todas las comunicaciones.

2. realiza un programa que te informe de cuanto vale cada comunicación y el total de dinero de todas las comunicaciones. En esta ocasión los datos de la duración de las comunicaciones y la tarifa por segundos se encuetran en este [fichero](comunicaciones.txt) donde en la primera línea te encuentras la tarifa, y en las restantes la duración de cda una de las comunicaciones expresdas en horas, minutos y segundos.



