---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---

### Práctica: Mediciones de rendimiento de Apache2 sirviendo páginas dinámicas

#### (7 tareas - 20 puntos)

Vamos a comparar el uso de memoria y el rendimiento de Apache2 sirviendo páginas dinámicas programadas con PHP. Para ello vamos a instalar un wordpress un servidor y vamos a realizar las siguientes pruebas:

    500 peticiones y 2 concurrentes
    5000 peticiones y 10 concurrentes
    10000 peticiones y 100 concurrentes

Hay que generar gráficas de uso de memoria y rendimiento donde se vea la comparativa entre las distintas formas de ejecutar PHP:

* Módulo php5-apache2
* Módulo php5-apache2 + acelerador apc
* Módulo php5-apache2 + varnish
* FPM-PHP + event
* FPM-PHP + event + acelerador apc
* FPM-PHP + event + varnish

Genera una documentación que al menos tenga los siguientes puntos:

1. Introducción. Explicación de los módulos de multiprocesamiento. Objetivos de la práctica.
2. Configuración de los escenarios:
	* Instalación del módulo php de apache2.
	* Instalación y configuración del acelerador apc
	* Instalación y configuración de vanish
	* Instalación y configuración de FPM-PHP con el módulo de multiprocesamiento event
	* Configuración del acelerador apc y vanish con la nueva configuración
3. Generación de las grafícas de uso de memoria: una para cada configuración en cada una de las cargas (18 en total).
4. Generación de las gráficas de rendimiento: una para cada carga, con 6 gráficas.
5. CONCLUSIONES. Lo más valorado en la tarea serán las conclusiones a las que llegas.

<div class='ejercicios' markdown='1'>

* **Tarea 1 (2 puntos):