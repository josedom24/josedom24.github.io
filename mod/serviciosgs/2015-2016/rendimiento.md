---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Mediciones de rendimiento de Apache2 sirviendo páginas dinámicas

#### (9 tareas - 30 puntos)(6 tareas obligatorias - 12 puntos)

Vamos a comparar el uso de memoria y el rendimiento de Apache2 sirviendo páginas dinámicas programadas con PHP. Para ello vamos a instalar un wordpress un servidor y vamos a realizar las siguientes pruebas:

    500 peticiones y 2 concurrentes
    5000 peticiones y 10 concurrentes
    10000 peticiones y 100 concurrentes

Hay que generar gráficas de uso de memoria y rendimiento donde se vea la comparativa entre las distintas formas de ejecutar PHP:

* Módulo php5-apache2
* Módulo php5-apache2 + memcached
* Módulo php5-apache2 + varnish
* FPM-PHP + event
* FPM-PHP + event + memcached
* FPM-PHP + event + varnish

Genera una documentación que al menos tenga los siguientes puntos:

1. Introducción. Explicación de los módulos de multiprocesamiento. Objetivos de la práctica.
2. Configuración de los escenarios:
	* Instalación del módulo php de apache2.
	* Instalación y configuración de memcached
	* Instalación y configuración de vanish
	* Instalación y configuración de FPM-PHP con el módulo de multiprocesamiento event
	* Configuración de memcached y vanish con la nueva configuración
3. Generación de las grafícas de uso de memoria: una para cada configuración en cada una de las cargas (18 en total).
4. Generación de las gráficas de rendimiento: una para cada carga, con 6 gráficas.
5. CONCLUSIONES. Lo más valorado en la tarea serán las conclusiones a las que llegas.

<div class='ejercicios' markdown='1'>

Antés de empezar a escribir la documentación, documenta en redmine y enseña al profesor las siguientes tareas:

* **Tarea 1 (2 punto)(Obligatorio):**Documenta la instalación del módulo php de apache2. Muestra wordpress funcionando con el módulo php de apache2. Realiza una comprobación de que, efectivamente, se está usando el módulo php.
* **Tarea 2 (2 puntos)(Obligatorio):**Documenta la instalación y configuración de memcached. Entrega una comprobación de que memcached está funcionando.
* **Tarea 3 (2 puntos)(Obligatorio):**Documenta la instalación y configuración de varnish. Entrega una comprobación de que varnish está funcionando.
* **Tarea 4 (2 puntos)(Obligatorio):**Documenta la instalación y configuración de FPM-PHP con el módulo de multiprocesamiento event (desinstala el memcached y vanish). Muestra wordpress funcionando con FPM-PHP. Realiza una comprobación de que, efectivamente, se está usando FPM-PHP.
* **Tarea 5 (2 puntos)(Obligatorio):**Entrega y muestra una comprobación de que memcached está funcionando con la nueva configuración.
* **Tarea 6 (2 puntos)(Obligatorio):**Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.

Ahora puedes realizar el trabajo y generar la documentación en pdf requerida, teniendo en cuenta los siguientes puntos:

* **Tarea 7 (4 puntos)**: Introducción del trabajo. Explica los objetivos de la práctica. Explica los módulos de multiprocesamiento.
* **Tarea 8 (6 puntos)**: Generación de las gráficas.
* **Tarea 9 (8 puntos)**: Conclusiones. Explica razonadamente a las conclusiones que has llegado.