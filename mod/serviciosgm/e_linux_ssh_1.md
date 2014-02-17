---
layout: index

title: Servicios de red 
tagline: CFGM SMR
---
### Ejercicio: Gestión remota usando SSH

####  Instalación y configuración del servidor ssh

Para instalar el servidor y el cliente ssh debemos instalar mediante apt-get el paquete ssh que contiene tanto la aplicación servidora como la aplicación cliente:

        apt-get install ssh

Los archivos de configuración son:

        /etc/ssh/ssh_config: Archivo de configuración del cliente ssh
        /etc/ssh/sshd_config: Archivo de configuración del servidor ssh

Por seguridad se suele no permitir la conexión del root al servidor para ello, se debe modificar el archivo /etc/ssh/sshd_config, y poner la opción PermitRootLogin a no.

        PermitRootLogin no

Para reiniciar el servicio ssh:

        service ssh restart

#### Conectarse al servidor ssh

Tenemos que asegurarnos que tenemos instalado el cliente ssh, para ello:

        apt-get install openssh-client

Para acceder desde el cliente al servidor tecleamos:

        ssh usuario@servidor

Por ejemplo:

        ssh pepito@192.168.1.15
        ssh jaimito@informatica.gonzalonazareno.org

La primera vez que se conecte a un servidor, tenemos que guardar el certificado de autentificación del servidor, por lo tanto a la pregunta 'Are you sure you want to continue connecting (yes/no)?' debemos responder 'yes' ya que de lo contrario la comunicación se cortará.

Para salir de la sesión escribiremos exit.

Si estamos usando un cliente Windows tenemos que usar un cliente ssh, el más conocido es putty.

#### Servicios adicionales

##### Ejecución remota de aplicaciones gráficas

Mediante ssh existe la posibilidad de ejecutar aplicaciones gráficas en el servidor y manejarlas y visualizarlas en el cliente. El servidor ssh deberá tener activada la redirección del protocolo X, es decir, deberá tener el siguiente parámetro en el archivo de configuración /etc/ssh/ssh_config:

        ForwardX11 yes

Para ejecutar aplicaciones gráficas, accedemos al ssh con la opción -X

        ssh -X cnice@192.168.1.239

y posteriormente podemos ejecutar cualquier aplicación gráfica, por ejemplo gedit.

##### Transferir ficheros con ssh

Para copiar un fichero de un ordenador a otro de forma segura, encriptando la información, podemos usar la herramienta scp de la siguiente manera:

Copiar un fichero a un ordenador remoto

        scp archivo_local usuario@servidor:/dir_remoto/archivo_remoto

Copiar un fichero desde un ordenador remoto

        scp usuario@servidor:/directorio_remoto/archivo_remoto archivo_local

Por ejemplo, para copiar un archivo que tengo en mi directorio personal del cliente, a un directorio del servidor:

        scp /home/usuario/documento.odt usuario@servidor.iesgn.org:/home/usuario




<div class='ejercicios' markdown='1'>
##### **Ejercicios**

1) Instala el servidor ssh en nuestro servidor, y comprueba lo siguiente:

* Modificación en el fichero de configuración para no permitir el acceso del root.
* Accede al servidor con un usuario que no sea root.
* Accede al servidor desde un cliente Windows con putty.

2) Modifica el servidor ssh para poder ejecutar aplicaciones gráficas (hazlo en el cliente ubuntu) accede al servidor con la posibilidad de ejecutar aplicaciones gráfica. Ejecuta una aplicación gráfica.

3) Copia un fichero desde el escritorio de tu cliente a la carpeta personal de un usuario del servidor.

</div>


[Volver](index)
