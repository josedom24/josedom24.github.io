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

Las características de escabilidad no están activades en el plan gratuito de heroku.

### Redundancia

En el momento en que podemos tener varios dynos detrás de una balanceado de carga, nuestra aplicación es redundante. Es decir, si algún dyno tiene un problema, lo demás responderían las peticiones.

### Aislamiento y seguridad

Cada uno de los dynos está aislado de los demás. Esto nos ofrece seguridad frente a la ejecución de procesos en otros dynos, además también nos ofrece protección para que ningún dyno consuma todos los recursos de la máquina. 

### Sistema de archivo efímero

Cada dyno posee un sistema de archivo cuya principal característica es que es efímero. Es decir los datos de nuestra aplicación (por ejemplo ficheros subidos) no son accesibles desde otros dynos, y si reiniciamos el dyno estos datos se pierden. Es muy recomendable tener los datos de la aplicación en un sistema externo, por ejemplo un almacen de objetos, como Amanzon S3 o OpenStack Swift.

### Direccionamiento IP

Cuando tenemos varios dynos, cada uno de eelos puede estar ejecutandose en máquinas diferentes. El acceso a nuestra aplicación siempre se hace desde un balanceador de carga ([routers](https://devcenter.heroku.com/articles/http-routing)). Esto significa que los dynos no tienen una ip estática, y el acceso a ellos siempre se hace a la dirección IP que tiene el balanceador. Cuando se reincia un dyno se puede ejecutar en otra máuina, y por lo tanto puede cambiar de dirección IP.

### Interfaces de red

Cada dyno tiene una interfaz de red con un direccionamiento privado /30, en el rango 172.16.0.0/12