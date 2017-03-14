---
layout: index

title: Lenguaje de marcas
tagline: CFGS ASIR
---

### Peticiones a REST API

1. Redmine (sin auth, XML)

		curl http://dit.gonzalonazareno.org/redmine/projects.xml

2. Loteria (sin auth,JSON)

		curl http://api.elpais.com/ws/LoteriaNavidadPremiados\?n\=12345

3. Redmine (KEY, XML)

		curl http://dit.gonzalonazareno.org/redmine/projects.xml\?key\=5921fa7b1ceafcaa23b85233f800b1c209473543

4. Redmine (KEY, JSON)

		curl http://dit.gonzalonazareno.org/redmine/projects.json\?key\=5921fa7b1ceafcaa23b85233f800b1c209473543

5. Redmine (KEY,XML)

		curl http://dit.gonzalonazareno.org/redmine/issues.xml\?status_id\=open\&limit\=5\&project_id\=asir1\&key\=5921fa7b1ceafcaa23b85233f800b1c209473543

6. Openweathermap (KEY, XML)

		curl http://api.openweathermap.org/data/2.5/weather\?\q=Sevilla\&mode\=xml\&units\=metric\&APPID\=cebee4a82fbddad71af7804bc82a3303z

7. Openweathermap (KEY, JSON)

		curl http://api.openweathermap.org/data/2.5/weather\?\q=Sevilla\&mode\=json\&units\=metric\&APPID\=cebee4a82fbddad71af7804bc82a3303

8. 


[Volver](index)
