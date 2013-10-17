---
layout: index

title: Servicios de Red e Internet
tagline: CFGS ASIR
---
### Ejercicio: Autentificación con usuarios del sistema

Otro método que vamos a estudiar es usar los usuarios del sistema para la autentificación, aunque existe un módulo para ello [mod_auth_pam](http://pam.sourceforge.net/mod_auth_pam/), no lo vamos a usar ya que lleva mucho tiempo no soportado, vamos a usar el módulo [mod_auth_external](http://code.google.com/p/mod-auth-external/) que es un módulo de Apache que permite autenticar los usuarios contra servicios externos: nosotros vamos a usar pwauth que permite verificar usuarios y contraseñas del sistema.

        # apt-get install libapache2-mod-auth-external pwauth

 En el fichero de configuración del Virtual Host tendríamos que incluir algo así:

        DefineExternalAuth pwauth_auth pipe /usr/sbin/pwauth
        <Directory /var/www/privado2>
         AuthType Basic
         AuthBasicProvider external
         AuthExternal pwauth_auth
         AuthName "this text will be display on auth box"
         Require valid-user
        </Directory>

[Volver](index)
