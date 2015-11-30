---
layout: index

title: Docker
tagline: josedom24.github.io
---
<div id="preview" preview=""><h1><a id="Introduccin_a_Docker_0"></a>Introducción a Docker</h1>
<p>Docker es un proyecto <a href="https://github.com/docker/docker"><em>open source</em></a> que ha revolucionado la manera de desarrollar software gracias a la sencillez con la que permite gestionar contenedores. Los contenedores LXC (LinuX Containers) son un concepto relativamente antiguo y utilizado desde hace tiempo por grandes empresas como Amazon o Google, pero cuyo gestión era complicada. Sin embargo, Docker define APIs y herramientas de línea de comandos que hacen casi trivial la creación, distribución y ejecución de contenedores. De ahí que el lema de Docker sea: “Build, Ship and Run. Any application, Anywhere” y se haya convertido en una herramienta fundamental tanto para desarrolladores como para administradores de sistemas.</p>
<p>Podríamos definir un contenedor Docker como una máquina virtual ligera, que corre sobre un sistema operativo Linux pero con su propio sistema de ficheros, su propio espacio de usuarios y procesos, sus propias interfaces de red… por lo que se dice que son sistemas <em>aislados</em>. Las características principales de Docker son su portabilidad, su inmutabilidad y su ligereza:<br><br></p>
<h3><a id="Portabilidad_6"></a>Portabilidad</h3>
<p>Un contenedor Docker es ejecutado por lo que se denomina el <em>Docker Engine</em>, un demonio que es fácilmente instalable en prácticamente todas las distribuciones Linux. Un contenedor ejecuta una imagen de docker, que es una representación del sistema de ficheros y otros metadatos que el contenedor va a utilizar para su ejecución. Una vez que hemos generado una imagen de Docker, ya sea en nuestro ordenador o vía una herramienta externa, esta imagen podrá ser ejecutada por cualquier Docker Engine, independientemente del sistema operativo y la infraestructura que haya por debajo.</p>
<h3><a id="Inmutabilidad_10"></a>Inmutabilidad</h3>
<p>Una aplicación la componen tanto el código fuente como las librerías del sistema operativo y del lenguaje de programación necesarias para la ejecución de dicho código. Estas dependencias dependen a su vez del sistema operativo donde nuestro código va a ser ejecutado, y por esto mismo ocurre muchas veces aquello de que <em>“no sé, en mi máquina funciona”</em>. Sin embargo, el proceso de instalación de dependencias en Docker no depende del sistema operativo, si no que este proceso se realiza cuando se genera una imagen de docker. Es decir, una imagen de docker (también llamada <em>repositorio</em> por su parecido con los repositorios de <em>git</em>) contiene tanto el código de la aplicación como las dependencias que necesita para su ejecución. Una imagen se genera una vez y puede ser ejecutada las veces que sean necesarias, y siempre ejecutará con las misma versión del código fuente y sus dependencias, por lo que se dice que es inmutable. Si unimos inmutabilidad con el hecho de que Docker es portable, decimos que Docker es una herramienta fiable, ya que una vez generada una imagen, ésta se comporta de la misma manera independientemente del sistema operativo y de la infraestructura donde se esté ejecutando.</p>
<h3><a id="Ligereza_14"></a>Ligereza</h3>
<p>Los contenedores Docker corriendo en la misma máquina comparten entre ellos el sistema operativo, pero cada contenedor es un proceso independiente con su propio sistema de ficheros y su propio espacio de procesos y usuarios (para este fin Docker utiliza <em>cgroups</em> y <em>namespaces</em>, recursos de aislamiento basados en el kernel de Linux). Esto hace que la ejecución de contenedores sea mucho más ligera que otros mecanismos de virtualización. Comparemos por ejemplo con otra tecnología muy utilizada como es Virtualbox. Virtualbox permite del orden de 4 ó 5 máquinas virtuales en un ordenador convencional, mientras que en el mismo ordenador podremos correr cientos de containers sin mayor problema, además de que su gestión es mucho más sencilla.<br><br></p>
<h2><a id="Componentes_de_Docker_19"></a>Componentes de Docker</h2>
<p>Docker está formado fundamentalmente por tres componentes:</p>
<ul>
<li>Docker Engine</li>
<li>Docker Client</li>
<li>Docker Registry<br><br></li>
</ul>
<h3><a id="Docker_Engine_o_Demonio_Docker_27"></a>Docker Engine o Demonio Docker:</h3>
<p>Es un demonio que corre sobre cualquier distribución de Linux y que expone una API externa para la gestión de imágenes y contenedores (y otras entidades que se van añadiendo en sucesivas distribuciones de docker como volúmenes o redes virtuales). Podemos destacar entre sus funciones principales:</p>
<ul>
<li>Creación de imágenes docker.<br><br></li>
<li>Publicación de imágenes en un Docker Registry o Registro de Docker (otro componente Docker que se explicará a continuación).<br><br></li>
<li>Descarga de imágenes desde un Registro de Docker<br><br></li>
<li>Ejecución de contenedores usando imágenes locales.<br><br></li>
</ul>
<p>Otra función fundamental del Docker Engine es la gestión de los contenedores en ejecución, permitiendo parar su ejecución, rearrancarla, ver sus logs o sus estadísticas de uso de recursos.<br><br></p>
<h3><a id="Docker_Client_o_Cliente_Docker_38"></a>Docker Client o Cliente Docker</h3>
<p>Es cualquier herramienta que hace uso de la api remota del Docker Engine, pero suele hacer referencia al comando <em>docker</em> que hace las veces de herramienta de línea de comandos (cli) para gestionar un Docker Engine. La <em>cli</em> de docker se puede configurar para hablar con un Docker Engine local o remoto, permitiendo gestionar tanto nuestro entorno de desarrollo local, como nuestros servidores de producción. Los comandos de docker más comunes son:</p>
<ul>
<li><em>docker info</em>: da información acerca de la cantidad de contenedores e imágenes que está gestionando la máquina actual, así como los plugins actualmente instalados.<br><br></li>
<li><em>docker images</em>: lista información de las imágenes que se encuentran disponibles en la máquina (nombre, id, espacio que ocupa, el tiempo que transcurrió desde que fue creada).<br><br></li>
<li><em>docker build</em>: crea una imagen desde el fichero <code>Dockerfile</code> del directorio actual.<br><br></li>
<li><em>docker pull &lt;imagen&gt;:&lt;version&gt;</em>: descarga en la máquina actual la versión de la imagen indicada. En caso de no indicar la versión descarga todas las que estén disponibles.<br><br></li>
<li><em>docker push &lt;imagen&gt;:&lt;version&gt;</em>: sube la versión de la imagen indicada a un Registro de Docker, permitiendo su distribución a otras máquinas.<br><br></li>
<li><em>docker rmi &lt;imagen&gt;:&lt;version&gt;</em>: elimina una imagen de la máquina actual.<br><br></li>
<li><em>docker run &lt;imagen&gt;:&lt;version&gt;</em>: crea un contenedor a partir de una imagen. Este comando permite multitud de parámetros, que son actualizados para cada versión del Docker Engine, por lo que para su documentación lo mejor es hacer referencia a la <a href="https://docs.docker.com/engine/reference/run/">página oficial</a>.<br><br></li>
<li><em>docker ps</em>: muestra los contenedores que están corriendo en la máquina. Con el flag <code>-a</code> muestra también los contenedores que están parados.<br><br></li>
<li><em>docker inspect contenedor</em>: muestra información detallada de un contenedor en formato json. Se puede acceder a un campo particular con el comando <code>docker inspect -f '{{.Name}}' contenedor</code>.<br><br></li>
<li><em>docker stop contenedor</em>: para la ejecución de un contenedor.<br><br></li>
<li><em>docker start contenedor</em>: reanuda la ejecución de un contenedor.<br><br></li>
<li><em>docker rm contenedor</em>: elimina un contenedor. Para borrar todos los contenedores de una máquina se puede ejecutar el comando <code>docker rm -fv $(docker ps -aq)</code>.<br><br></li>
<li><em>docker logs contenedor</em>: muestra los logs de un contenedor.<br><br></li>
<li><em>docker stats contenedor</em>: muestra las estadísticas de ejecución de un contenedor, como son la memoria utilizada, la CPU, el disco…<br><br></li>
<li><em>docker exec contenedor comando</em>: ejecuta un comando en un contenedor. Útil para depurar contenedores en ejecución con las opciones <code>docker exec -it contenedor bash</code>.<br><br></li>
<li><em>docker volume ls</em>: lista los volúmenes existentes en la máquina. Para un listado completo de los comandos relacionados con volúmenes ejecuta <code>docker volume --help</code>.<br><br></li>
<li><em>docker network ls</em>: lista las redes existentes en la máquina. Para un listado completo de los comandos relacionados con redes ejecuta <code>docker network --help</code>.</li>
</ul>
<h3><a id="Docker_Registry_o_Registro_Docker_61"></a>Docker Registry o Registro Docker</h3>
<p>El Registro es otro componente de Docker que suele correr en un servidor independiente y donde se publican las imágenes que generan los Docker Engine de tal manera que estén disponibles para su utilización por cualquier otra máquina. Es un componente fundamental dentro de la arquitectura de Docker ya que permite distribuir nuestras aplicaciones. El Registro de Docker es un proyecto <a href="https://github.com/docker/distribution"><em>open source</em></a> que puede ser instalado gratuitamente en cualquier servidor, pero Docker ofrece <em>Dockerhub</em>, un sistema <em>SaaS</em> de pago donde puedes subir tus propias imágenes, acceder a imágenes públicas de otros usuarios, e incluso a imágenes oficiales de las principales aplicaciones como son: MySQL, MongoDB, RabbitMQ, Redis, etc.</p>
<p>El registro de Docker funciona de una manera muy parecida a <em>git</em> (de la misma manera que Dockerhub y us métodos de pago funcionan de una manera muy parecida a <em>Github</em>). Cada imagen, también conocida como repositorio, es una sucesión de capas. Es decir, cada vez que hacemos un build en local de nuestra imagen, el Registro de Docker sólo almacena el <strong>diff</strong> respecto de la versión anterior, haciendo mucho más eficiente el proceso de creación y distribución de imágenes.<br><br></p>
<h2><a id="Instalacin_de_Docker_67"></a>Instalación de Docker</h2>
<p>En la instalación de Docker queremos distinguir la instalación para el desarrollo en local, y la instalación en servidores para correr código en producción. En cuanto a la instalación en servidores de producción, la mayoría de proveedores de servicio: AWS, GCE, Azure, Digital Ocean… disponen de máquinas virtuales con versiones de Docker pre-instaladas. En cualquier caso, la instalación es bastante sencilla. Como el proceso varía un poco entre versiones de Docker, preferimos poner un enlace a la documentación oficial de la <a href="https://docs.docker.com/engine/installation/ubuntulinux/">instalación en Ubuntu</a>.</p>
<p>Para la instalación en local para desarrolladores, Docker ofrece la instalación de <a href="https://www.docker.com/docker-toolbox">Docker Toolbox</a>. Docker Toolbox instala en Mac y en Windows, y consiste de los componentes:</p>
<ul>
<li>Kitematic: UI de gestión de contenedores.</li>
<li>Docker Machine: herramienta para la creación de máquinas virtuales con Docker instalado. Incluye Virtualbox.</li>
<li>Docker Compose: herramienta para gestionar contenedores basada en definición de contenedores y sus relaciones en un formato <em>yml</em>.</li>
</ul>
<p>En este tutorial no explicaremos Kitematic por ser una herramienta en beta y en proceso de cambio, pero explicaremos un poco sobre cómo funcionan Docker Machine y Docker Compose.<br><br></p>
<h2><a id="Docker_Machine_80"></a>Docker Machine</h2>
<p>Docker Machine es un proyecto <a href="https://github.com/docker/machine"><em>open source</em></a> que como hemos dicho automatiza la creación de maquinas virtuales con Docker instalado. Incluye drivers para distintos proveedores de servicios en la nube, como AWS, GCE, Azure, Digital Ocean… y también para Virtualbox (ver lista completa de drivers <a href="https://docs.docker.com/machine/drivers/">aquí</a>). <strong>Virtualbox es la opción aconsejada</strong> para instalaciones de Docker en local, en lugar de instalar Docker directamente en tu ordenador personal. Esto es debido a que nos permitirá crear o destruir la instalación de Docker con mayor facilidad, actualizar la versión de Docker, o trabajar con distintas instalaciones de Docker a la vez para aislar entornos de aplicaciones.</p>
<p>La documentación de los comandos disponibles en Docker Machine puede ser consultada <a href="https://docs.docker.com/machine/reference/">aquí</a>, pero queremos destacar algunas buenas prácticas:</p>
<ul>
<li>Crea una máquina de Virtualbox para cada aplicación con la que trabajes. Aunque Docker aísla la ejecución de contenedores, siempre hay inter-relaciones como los puertos donde escuchan los distintos componentes, por lo que correr todas las aplicaciones en el mismo Virtualbox puede dar lugar a conflictos. Además, el driver de Virtualbox tiene algunos bugs que te obligarán a recrear la máquina cada cierto tiempo, tener entornos separados reduce los inconvenientes de este proceso.<br><br></li>
<li>El <a href="https://docs.docker.com/machine/drivers/virtualbox/">driver de Virtualbox</a> permite definir la memoria máxima (<code>--virtualbox-memory</code>) y el disco máximo (<code>--virtualbox-disk-size</code>) de la máquina virtual. Modifica estos valores si tu aplicación necesita muchos recursos.<br><br></li>
<li>Si tu presupuesto lo permite, puede ser conveniente crear tu máquina virtual de desarrollo en un proveedor de servicios como Amazon para no consumir recursos en tu ordenador personal, sobretodo si tu aplicación es muy pesada.<br><br></li>
<li>Haz uso del comando <code>eval "$(docker-machine env name)"</code> para auto-configurar tu Docker Client respecto a la maquina <code>name</code>, de tal manera que tus commandos de Docker se ejecuten en la máquina <code>name</code>.<br><br></li>
</ul>
<h2><a id="Docker_Compose_92"></a>Docker Compose</h2>
<p>Docker compose es otro proyecto <a href="https://github.com/docker/compose"><em>open source</em></a> que permite definir aplicaciones muilti-contenedor de una manera sencilla y declarativa. Es una herramienta ideal para gestionar entornos de desarrollo y de pruebas, o para procesos de integración continua como veremos en la próxima sesión.</p>
<p><em>docker-compose</em> es una alternativa más cómoda al uso del comando <em>docker run</em>, que resulta ingobernable cuando trabajamos con aplicaciones con varios componentes. Con Docker Compose se define un fichero <em>docker-compose.yml</em> que tiene esta forma:<br><br></p>
<pre><code><span class="hljs-attribute">web</span>:
  <span class="hljs-attribute">build</span>: .
  <span class="hljs-attribute">ports</span>:
   - <span class="hljs-string">"5000:5000"</span>
  <span class="hljs-attribute">links</span>:
   - redis
<span class="hljs-attribute">redis</span>:
  <span class="hljs-attribute">image</span>: redis
</code></pre>
<p><br>Donde estamos definiendo una aplicación que se compone de un contenedor definido desde un Dockerfile local, que escucha en el puerto 5000, y que hace uso de <em>redis</em> como un servicio externo. Dada esta definición, la manera de levantar la aplicación es simplemente:<br><br></p>
<pre><code>docker-compose up <span class="hljs-operator">-d</span>
</code></pre>
<p><em><br>docker-compose</em> acepta distintos comando, una lista completa puede encontrarse <a href="https://docs.docker.com/compose/reference/">aquí</a>. Destacar los siguientes puntos sobre <em>docker-compose</em>:</p>
<ul>
<li><code>docker-compose up -d</code> levanta la aplicación en modo demonio, <code>docker-compose up</code> la levanta en primer plano, mostrando los logs de los distintos contenedores. La ejecución sucesiva del comando <code>docker-compose up -d</code> sólo recrea los contenedores que hayan cambiado su imagen o su definición.<br><br></li>
<li><code>docker-compose up -d</code> no hace el build de las imágenes locales. Si deseas actualizar tu aplicación en base a los últimos cambios de tu código, necesitarás hacer <code>docker-compose build</code> antes de ejecutar <code>docker-compose up -d</code> nuevamente. Un truco para mejorar este proceso <br>es montar tu código como un volumen en el fichero <code>docker-compose.yml</code>, de tal manera que tu container siempre ve los últimos cambios en tu código fuente.<br><br></li>
</ul>
<p><em>docker-compose</em> permite definir prácticamente todos los flags que soporta el comando <em>docker run</em>, pero <em>docker-compose</em> es mucho más fácil de utilizar. Las opciones más comunes son:</p>
<ul>
<li><em>build</em>: para indicar que el container se construye desde un Dockerfile local.<br><br></li>
<li><em>image</em>: para indicar que el container corre un imagen remota.<br><br></li>
<li><em>command</em>: para redefinir el comando que ejecuta el container en lugar del comando definido en la imagen.<br><br></li>
<li><em>environment</em>: para definir variables de entorno en el contenedor. Se pueden pasar haciendo referencia a un fichero usando la propiedad <em>env_file</em>. Si la variable no tiene un valor dado, su valor se cogerá del entorno de shell que ejecuta el <code>docker-compose up</code>, lo que puede ser útil para pasar claves, por ejemplo.<br><br></li>
<li><em>links</em>: para definir relaciones entre contenedores.<br><br></li>
<li><em>ports</em>: para mapear los puertos donde el contenedor acepta conexiones.<br><br></li>
<li><em>volumes</em>: para definirir volúmes en el contenedor.<br><br></li>
<li><em>volumes_from</em>: para reusar los volúmenes de otro contenedor.</li>
</ul>
<p><a href="https://docs.docker.com/compose/compose-file/">Aquí</a> tenéis una lista completa y actualizada de las opciones que permite <em>docker-compose</em>.</p>
<h2><a id="Conclusin_134"></a>Conclusión</h2>
<p>Docker está teniendo un notable éxito y éste no ha venido de forma gratuita, sino porque es una tecnología disruptiva que implica una mejora tremenda en los procesos de desarrollo de software. Nosotros aconsejamos su conocimiento y utilización tanto por parte de desarrolladores como por parte de administradores de sistema, ya que todas las grandes firmas de la nube, como son Amazon, Google, Microsoft, IBM, Oracle… están metidos en la carrera de dar el mejor soporte posible para Docker. Esto se debe a que todas las empresas, pequeñas, medianas y grandes multinacionales, están haciendo uso de Docker para desarrollar y gestionar sus aplicaciones (valga como ejemplo el gobierno de los EE.UU), por lo que no adoptar esta tecnología (u otras similares que puedan aparecer) será una desventaja competitiva en los mercados tecnológicos.</p>
</div>
