---
layout: index

title: José Domingo Muñoz	
tagline: josedom24.github.io
---
## Introducción a PaaS usando heroku

[Heroku]() es una aplicación que nos oferece un servicio de Cloud Computing [PaaS]() (Plataforma como servicio). Como leemos en la [Wikipedia]() es propiedad de [Salesforce.com](www.salesforce.com) y es una de las primeras plataformas de computación en la nube, que fue desarrollada desde junio de 2007, con el objetivo de soportar solamente el lenguaje de programación Ruby, pero posteriormente se ha extendido el soporte a Java, Node.js, Scala, Clojure y Python y PHP.

### Características de heroku

La funcionalidad que nos ofrece heroku esta disponible con el uso de dynos, que son una adaptación de contenedor Linux y nos ofrece la capacidad de computo dentro de la plataforma.

Cada dyno ejecuta distintos procesos, por ejemplo ejecuta los servidores web y los servidores de bases de datos, o cualquier otro proceso que le indiquemos en un fichero Procfile. Las caraacteristicas principales de los dynos son:

### Escabilidad

Si, por ejemplo, tenemos muchas peticiones a nuestra aplicación podemos hacer un escalado horizontal, es decir, podemos crear más dynos que respondan las peticiones. La carga de peticiones se balanceará entre los dynos existentes. Además podemos hacer una escalabilidad vertical, en este caso lo que hacemos es cambiar las caracteristicas hardware de nuetro dyno, por ejemplo aumtentar la cantidad de RAM.

Las caracter´isticas de escabilidad no están activades en el plan gratuito de heroku.

###