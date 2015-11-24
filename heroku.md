---
layout: index

title: José Domingo Muñoz	
tagline: josedom24.github.io
---
## Introducción a PaaS usando heroku

[Heroku]() es una aplicación que nos ofrece un servicio de Cloud Computing [PaaS]() (Plataforma como servicio). Como leemos en la [Wikipedia]() es propiedad de [Salesforce.com](www.salesforce.com) y es una de las primeras plataformas de computación en la nube, que fue desarrollada desde junio de 2007, con el objetivo de soportar solamente el lenguaje de programación Ruby, pero posteriormente se ha extendido el soporte a Java, Node.js, Scala, Clojure y Python y PHP.

### Características de heroku

La funcionalidad que nos ofrece heroku esta disponible con el uso de dynos, que son una adaptación de contenedor Linux y nos ofrece la capacidad de computo dentro de la plataforma.

Cada dyno ejecuta distintos procesos, por ejemplo ejecuta los servidores web y los servidores de bases de datos, o cualquier otro proceso que le indiquemos en un fichero Procfile. Las características principales de los dynos son:

* Escabilidad: Si, por ejemplo, tenemos muchas peticiones a nuestra aplicación podemos hacer un escalado horizontal, es decir, podemos crear más dynos que respondan las peticiones. La carga de peticiones se balanceará entre los dynos existentes. Además podemos hacer una escalabilidad vertical, en este caso lo que hacemos es cambiar las características hardware de nuestro dyno, por ejemplo aumentar la cantidad de RAM. Las características de estabilidad no están activadas en el plan gratuito de heroku.
* Redundancia: En el momento en que podemos tener varios dynos detrás de una balanceado de carga, nuestra aplicación es redundante. Es decir, si algún dyno tiene un problema, lo demás responderían las peticiones.
* Aislamiento y seguridad: Cada uno de los dynos está aislado de los demás. Esto nos ofrece seguridad frente a la ejecución de procesos en otros dynos, además también nos ofrece protección para que ningún dyno consuma todos los recursos de la máquina. 
* Sistema de archivo efímero: Cada dyno posee un sistema de archivo cuya principal característica es que es efímero. Es decir los datos de nuestra aplicación (por ejemplo ficheros subidos) no son accesibles desde otros dynos, y si reiniciamos el dyno estos datos se pierden. Es muy recomendable tener los datos de la aplicación en un sistema externo, por ejemplo un almacén de objetos, como Amanzon S3 o OpenStack Swift.
* Direccionamiento IP: Cuando tenemos varios dynos, cada uno de eelos puede estar ejecutándose en máquinas diferentes. El acceso a nuestra aplicación siempre se hace desde un balanceador de carga ([routers](https://devcenter.heroku.com/articles/http-routing)). Esto significa que los dynos no tienen una ip estática, y el acceso a ellos siempre se hace a la dirección IP que tiene el balanceador. Cuando se reinicia un dyno se puede ejecutar en otra máquina, y por lo tanto puede cambiar de dirección IP.
* Interfaces de red: Cada dyno tiene una interfaz de red con un direccionamiento privado /30, en el rango 172.16.0.0/12. Por lo tanto cada dyno está conecta a una red independiente que no comparte con ningún otro dyno. Para acceder a él, como hemos indicado anteriormente, habrá que hacerlo a través de la ip pública que tiene asignada el balanceador de carga.

### Despliegue de una aplicación web en Heroku

En este ejemplo vamos a utilizar la capa gratuita que nos ofrece Heroku, que tiene las siguientes características:

* Podemos crear un dyno, que puede ejecutar un máximo de dos tipos de procesos. Para más información sobre la ejecución de los procesos ver: [https://devcenter.heroku.com/articles/process-model](https://devcenter.heroku.com/articles/process-model).
* Nuestro dyno utiliza 512 Mb de RAM
* Tras 30 minutos de inactividad el dyno se para (sleep), además debe estar parado 6 horas cada 24 horas.
* Podemos utilizar una base de datos postgreSQL con no más de 10.000 registros
* Para más información de los planes ofrecido por heroku puedes visitar: [https://www.heroku.com/pricing#dynos-table-modal](https://www.heroku.com/pricing#dynos-table-modal)

Para ampliar la funcionalidad de nuestra aplicación podemos añadir a nuestro dyno distintos [add-ons](https://elements.heroku.com/addons). Algunos lo podemos usar de forma gratuita y otros son de pago. El add-ons de mysql (ClearDB mysql) no lo podemos usar en el plan gratuito, por lo que vamos a usar una base de datos postgreSQL.

El objetivo de la siguiente práctica es instalar en local Drupal 8 usando una base de datos postgreSQL, y posteriormente hacer el despliegue a heroku. Vamos a realizar una configuración que nos permita ejecutar el CMS en local y en heroku. Vamos a realizar la instalación del CMS en el directorio git que clonemos de heroku, por lo tanto tendrá que coincidir con el DocumentRoot de nuestro servidor web local.

