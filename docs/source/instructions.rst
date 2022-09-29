Instrucciones:
==============

.. _step1:

1. Condiciones necesarias para acceder al servicio web
------------------------------------------------------

| El sitio web que se suscriba con Continental Assist para ofrecer el servicio, debe contratar un servicio de certificación https en donde sea colocada la herramienta a desarrollar.
| Continental Assist sólo se limitará a ofrecer la estructura resultante del servicio web con los datos resultantes de la compra del plan de servicio. El diseño de los frontend y la distribución será completa responsabilidad de los webmasters de los sites externos.
| Toda agencia o sitio externo que necesite utilizar los servicios en cuestión debe registrarse en el sistema como una agencia, por lo cual deben suministrar la siguiente información, adicional a la que normalmente se solicita, al personal de Continental Assist:

* Nombre del Dominio registrado correspondiente a su site (URL de la página web principal). Por ejemplo para el caso del portal **Agencia de Viajes Virtual**, sería  **“http://www.agenciadeviajesvirtual.com”**.
* Una vez registrado y activado el usuario, se le remitirá, vía correo electrónico, los datos de acceso al Sistema Continental Assist como agencia, así como el presente manual con la información de cómo implementar y utilizar los servicios y una clave de acceso **(“API KEY”)** única para que pueda utilizar el servicio.

**API KEY:** El consumo de los servicios necesita una clave encriptada, la cual es generada por el personal de sistemas de Continental Assist y representa la llave para validar el origen y el destino de las peticiones, esta llave es única e intransferible, es validada y asignada a cada agencia y cada tipo de usuario. El uso de la misma será detallado en **Cómo implementar e invocar los servicios web.**



.. _step2:

2. Flujo general
----------------

| Para un correcto uso de los servicios de Continental Assist es preciso conocer el flujo general del proceso de compra de la empresa, el cual se basa en los siguientes pasos respectivamente:

* Determinar los datos generales del viaje:
    * Definir Fecha de inicio y Fecha de fin.
    * Seleccionar Categoría.
    * Seleccionar Origen.
    * Seleccionar Destino.
    * Definir cantidad de pasajeros y la edad de los mismos.
* Seleccionar Plan:
    * Obtener información detallada de los planes (Beneficios y Precios).
    * Seleccionar plan.
* Suministrar Datos de los pasajeros.
* Seleccionar Beneficios Adicionales.
* Suminitrar datos de la tarjeta para la compra.
* Comprar.

| Luego de presionar el botón “Comprar”, se procede al proceso interno del sitio para sus respectivas validaciones y el envío de los datos correspondientes a la compra del plan de servicio.
| La respuesta que devuelva el sistema (sea positiva o negativa), tanto del servicio de compra como del resto de servicios, será enviada en formato interoperable (JSON) el cual debe ser formateado en la página receptora.



.. _step3:

3. Cómo implementar e invocar los servicios web
-----------------------------------------------

| La implementación de los servicios web corresponde a las operaciones de Cotización y Compra, los cuales son servicios ofrecidos por Continental Assist, utilizando para ello la interoperabilidad que ofrecen este tipo de tecnología. Los Servicios Web a presentar a continuación se desarrollaron utilizar el protocolo **REST**, el cual se caracteriza por no utilizar un contrato de servicio basado en **WSDL** y por utilizar el formato **JSON** en vez de **XML** para el transporte de las peticiones y respuestas.

| Para la implementación exitosa de los servicios deben llevarse a cabo las siguientes tareas:

* Incluir dentro de los **headers** de la petición el siguiente parámetro como Key: “Content-Type”, y como Value: “application/x-www-form-urlencoded”.
* Incluir dentro de los **headers** de la petición el siguiente parámetro como Key: “PHP-AUTHUSER”, y como Value la API KEY suministrada por Continental Assist.
* Los servicios web de compra, reciben como parámetros la información de los formularios, estructuradas en formato JSON, pasados como valores **POST.**

.. image:: /images/img_consulta_categorias.jpg

.. rubric:: (NOTA: La ruta “demo.continentalassist.com/restapi/v1/” es únicamente para fines de pruebas y desarrollo de los servicios).


.. centered:: Listado de Servicios

+----------------------+----------------------------------------+------------------------+
| Nombre del servicio  | Descripción y Respuesta                |  Parametros Requeridos |
+======================+========================================+========================+
| consulta_pais        | | Este webservice devuelve id y nombre | - ps                   | 
|                      | | de países al que se debe seleccionar |                        |
|                      | | el país desde donde se está haciendo |                        |
|                      | | la petición. (Este valor es requerido|                        |
|                      | | como parámetro en cada uno de los    |                        |
|                      | | servicios).                          |                        |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |    "resultado": [                      |                        |
|                      |    {                                   |                        |
|                      |      "id": "47",                       |                        |
|                      |      "pais": "Americas"                |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "20",                       |                        |
|                      |      "pais": "Antigua and Barbuda"     |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "1",                        |                        |
|                      |      "pais": "Argentina"               |                        |
|                      |    },                                  |                        |
|                      |    {                                   |                        |
|                      |      "id": "36",                       |                        |
|                      |      "pais": "Aruba"                   |                        |
|                      |    }                                   |                        |
|                      |    ],                                  |                        |
|                      |    "cantidad": 4,                      |                        |
|                      |    "error": false                      |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_categorias| | Devuelve el id y el nombre de las    | - ps                   | 
| | _x_pais_dias       | | categorías correspondientes a los    | - id_lenguaje          |
|                      | | el país desde donde se está haciendo | - id_pais              |
|                      | | a las características de la agencia  | - fecha_desde          |
|                      | | solicitante.                         | - fecha_hasta          |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "id_categoria": "24",              |                        |
|                      |     "categoria": "Planes por Viaje"    |                        |
|                      |   },                                   |                        |
|                      |   {                                    |                        |
|                      |     "id_categoria": "23",              |                        |
|                      |     "categoria": "Anuales-Multiviajes" |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 2,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_origenes  | | Devuelve id y nombre de paises que   | - ps                   | 
|                      | | determinan los origenes permitidos   |                        |
|                      | | para Continental Assist.             |                        |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "iso_country": "AL",               |                        |
|                      |     "description": "Albania"           |                        |
|                      |   },                                   |                        |
|                      |   {                                    |                        |
|                      |     "iso_country": "DE",               |                        |
|                      |     "description": "Alemania"          |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 2,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_destinos  | | Devuelve id y nombre de lugares que  | - ps                   | 
|                      | | determinan los destinos permitidos   |                        |
|                      | | para Continental Assist.             |                        |
|                      |                                        |                        |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "id_destino": "1",                 |                        |
|                      |     "descripcion_destino": "Europa"    |                        |
|                      |   },                                   |                        |
|                      |   {                                    |                        |
|                      |     "id_destino": "2",                 |                        |
|                      |     "descripcion_destino": "Mundial"   |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 2,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_planes    | | Devuelve el id del plan, el nombre   | - ps                   | 
| | (deprecated)       | | del plan, los precios individuales y | - dias                 |
| | Sustituido por:    | | grupales calculados en base a la     | - edades [edades]      |
| | consulta_planes    | | cantidad de pasajeros y sus edades   | - id_categoria         |
| | _grupal            |                                        | - id_destino           |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "id": "21",                        |                        |
|                      |     "valor": "21",                     |                        |
|                      |     "nombre": "Traveler",              |                        |
|                      |     "precio": "348.00",                |                        |
|                      |     "precio_adulto_mayor": "522.00",   |                        |
|                      |     "moneda": "USD",                   |                        |
|                      |     "edad_maxima_sin_incremento": "70",|                        |
|                      |     "acepta_pago_tdc": "SI",           |                        |
|                      |     "precio_grupal": "870.00"          |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 1,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | consulta_beneficios| | Devuelve el id_beneficio, el nombre  | - ps                   | 
| | _planes_costos     | | de los beneficios y, dentro de otro  | - id_lenguaje          |
|                      | | arreglo, el id_plan y el valor de    | - id_pais              |
|                      | | cada uno de los beneficios para      | - id_categoria         |
|                      | | dicho plan.                          | - id_planes            |
|                      |                                        | - [id_planes]          |
|                      | | Ejemplo Respuesta:                   |                        |
|                      |                                        |                        |
|                      | >>>                                    |                        |
|                      | {                                      |                        |
|                      |   "resultado": [                       |                        |
|                      |   {                                    |                        |
|                      |     "id_beneficio": "1",               |                        |
|                      |     "nombre_beneficio": "Asistencia    |                        |
|                      |               médica por accidente",   |                        |
|                      |     "planes": [                        |                        |
|                      |        {                               |                        |
|                      |           "id_plan": "114",            |                        |
|                      |           "valor": "USD 15.000"        |                        |
|                      |        }                               |                        |
|                      |        {                               |                        |
|                      |           "id_plan": "116",            |                        |
|                      |           "valor": "USD/EUR 30.000"    |                        |
|                      |        }                               |                        |
|                      |        {                               |                        |
|                      |           "id_plan": "117",            |                        |
|                      |           "valor": "USD 50.000"        |                        |
|                      |        }                               |                        |
|                      |        {                               |                        |
|                      |           "id_plan": "119",            |                        |
|                      |           "valor": "USD 100.000"       |                        |
|                      |        }                               |                        |
|                      |      ]                                 |                        |
|                      |   }                                    |                        |
|                      |   ],                                   |                        |
|                      |   "cantidad": 1,                       |                        |
|                      |   "error": false                       |                        |
|                      | }                                      |                        |
|                      |                                        |                        |
+----------------------+----------------------------------------+------------------------+
| | comprar            | | Devuelve codigo del vouchers y el    | - ps                   | 
|                      | | link para visualizar dicho voucher.  | - origen               |
|                      |                                        | - destino              |
|                      | | Ejemplo Respuesta:                   | - desde                |
|                      |                                        | - hasta                |
|                      | >>>                                    | - id_categoria         |
|                      | {                                      | - id_plan              |
|                      |   "resultado": [                       | - contacto             |
|                      |   {                                    |                        |
|                      |     "codigo": "CA-12345-00",           | | [nombre_contacto     |
|                      |     "link_voucher":                    | | telefono_contacto    |
|                      |  "https://continentalassist.co/backmin | | email_contacto]      |
|                      |  /voucher.php?idv=CA-A43LCH-1-MX&idv5  |                        |
|                      |  =spa"                                 | - beneficiarios        |
|                      |   }                                    |                        |
|                      |   ],                                   | | [nombre              |
|                      |   "cantidad": 1,                       | | apellido             |
|                      |   "error": false                       | | fechaNac             |
|                      | }                                      | | edad                 |
|                      |                                        | | pasaporte            |
|                      |                                        | | email                |
|                      |                                        | | telefono             |
|                      |                                        | | beneficios           |
|                      |                                        | | _adicionales [       |
|                      |                                        | |     id_beneficio     |
|                      |                                        | |     _adicional       |
|                      |                                        | |   ]                  |
|                      |                                        | | ]                    |
|                      |                                        |                        |
|                      |                                        | - ip                   |
|                      |                                        | - forma_pago           |
|                      |                                        | - inputCardNumber      |
|                      |                                        | - inputMonth           |
|                      |                                        | - inputYear            |
|                      |                                        | - inputCVV2            |
|                      |                                        | - totalgeneral         |
|                      |                                        | - inputNameCard        |
+----------------------+----------------------------------------+------------------------+


.. centered:: Ejemplos


+-----------------------------+-----------------------------------------------+------------------------------+
| Servicio                    | Ejemplo de JSON Requerido (Body)              | Formato                      |
+=============================+===============================================+==============================+
| consulta_pais               | >>>                                           | | **ps:** Dominio registrado |
|                             | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com"  |                              |
|                             | }                                             |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| | consulta_categorias       | >>>                                           | | **ps:** Dominio registrado | 
| | _x_pais_dias              | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com", | | **id_lenguaje:** ('span'   |
|                             | "id_lenguaje":"spa",                          | | : español, 'eng': ingles). |
|                             | "id_pais":11,                                 | | **id_pais:** id_selecciona |
|                             | "fecha_desde":"09-06-2017",                   | | do del servicio            |
|                             | "fecha_hasta":"13-06-2017"                    | | 'consulta_pais'            |
|                             | }                                             |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| consulta_origenes           | >>>                                           | | **ps:** Dominio registrado |
|                             | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com"  |                              |
|                             | }                                             |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| consulta_destinos           | >>>                                           | | **ps:** Dominio registrado |
|                             | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com"  |                              |
|                             | }                                             |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| | consulta_planes           | Sustituido por:                               | | **ps:** Dominio registrado | 
| | (**Deprecated**)          | consulta_planes_grupal                        | | correspondiente a su site. |
|                             |                                               | | **dias:** Un entero que    |
|                             | >>>                                           | | indique la cantidad de     |
|                             | {                                             | | días del viaje             |
|                             | "ps":"http://www.agenciadeviajesvirtual.com", | | **edades:** Un arreglo con |
|                             | "dias":120,                                   | | las edades de los          |
|                             | "edades":[20,75],                             | | pasajeros                  |
|                             | "id_categoria":24,                            | | **id_categoria:** id       |
|                             | "id_destino":2                                | | seleccionado del servicio  |
|                             | }                                             | | consulta_categorias        |
|                             |                                               | | **id_destino:** id         |
|                             |                                               | | seleccionado del servicio  |
|                             |                                               | | consulta_destinos          |
+-----------------------------+-----------------------------------------------+------------------------------+
| | consulta_beneficios       | >>>                                           | | **ps:** Dominio registrado | 
| | _planes_costos            | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com", | | **id_lenguaje:** ('span'   |
|                             | "id_lenguaje":"spa",                          | | : español, 'eng': ingles). |
|                             | "id_pais":11,                                 | | **id_pais:** id_selecciona |
|                             | "id_categoria":22,                            | | do del servicio            |
|                             | "id_planes":["114","116","117","119"]         | | 'consulta_pais'            |
|                             | }                                             | | **id_categoria:** id       |
|                             |                                               | | seleccionado del servicio  |
|                             |                                               | | 'consulta_categorias       |
|                             |                                               | | _x_pais_dias'              |
|                             |                                               | | **id_planes:** (arreglo)   |
|                             |                                               | | id o grupo de ids          |
|                             |                                               | | seleccionados del servicio |
|                             |                                               | | 'consulta_planes_grupal'   |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| | consulta_beneficios       | >>>                                           | | **ps:** Dominio registrado | 
| | _adicionales              | {                                             | | correspondiente a su site. |
|                             | "ps":"localhost",                             | | **id_categoria:** id       |
|                             | "id_categoria":24,                            | | seleccionado del servicio  |
|                             | "id_plan":21                                  | | 'consulta_categorias       |
|                             | }                                             | | _x_pais_dias'              |
|                             |                                               | | **id_plan:** id            |
|                             |                                               | | seleccionado del servicio  |
|                             |                                               | | 'consulta_planes_grupal'   |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+
| | comprar                   | >>>                                           | | **ps:** Dominio registrado | 
|                             | {                                             | | correspondiente a su site. |
|                             | "ps":"http://www.agenciadeviajesvirtual.com", | | **id_origen:** id          |
|                             | "origen": "CO",                               | | seleccionado del servicio  |
|                             | "destino": 2,                                 | | 'consulta_origen'          |
|                             | "desde": "09/06/2017",                        | | **id_destino:** id         |
|                             | "hasta": "13/06/2017",                        | | seleccionado del servicio  |
|                             | "id_categoria": 24,                           | | 'consulta_destino'         |
|                             | "id_plan": 21,                                | | **desde:** Fecha de inicio |
|                             | "familiar": "0",                              | | del viaje                  |
|                             | "contacto": {                                 | | formato DD/MM/YYYY         |
|                             |   "nombre_contacto": "CONTACTO",              | | **hasta:** Fecha de inicio |
|                             |   "telefono_contacto": "04121234556",         | | del viaje                  |
|                             |   "email_contacto": "contacto@gmail.com"      | | formato DD/MM/YYYY         |
|                             |   },                                          | | **id_categoria:** id       |
|                             | "beneficiarios": [{                           | | seleccionado del servicio  |
|                             |   "nombre": "BENEFICIARIO",                   | | 'consulta_categorias       |
|                             |   "apellido": "UNO",                          | | _x_pais_dias'              |
|                             |   "fechaNac": "01/01/1941",                   | | **id_plan:** id            |
|                             |   "edad": "76",                               | | seleccionado del servicio  |
|                             |   "pasaporte": "1234567",                     | | 'consulta_planes_grupal'   |
|                             |   "email": "beneficiario1@gmail.com",         | | (Opcional)                 |
|                             |   "telefono": "04124121212",                  | | **familiar:** El valor '1' |
|                             |   "beneficios_adicionales":[35,36]            | | (en caso de requerir Plan  |
|                             |   },                                          | | Familiar). Por defecto     |
|                             |   {                                           | | este valor se capturará    |
|                             |   "nombre": "BENEFICIARIO",                   | | en '0' (cero).             |
|                             |   "apellido": "DOS",                          | | Nota: Soló las peticiones  |
|                             |   "fechaNac": "01/01/1992",                   | | que cumplan conlos         |
|                             |   "edad": "25",                               | | requerimientos mínimos y   |
|                             |   "pasaporte": "1234567",                     | | las siguientes categorías: |
|                             |   "email": "beneficiario2@gmail.com",         | | Anuales Multiviajes        |
|                             |   "telefono": "04124121212",                  | | (id 23) y                  |
|                             |   "beneficios_adicionales":[35]               | | Planes por Viaje (id 24),  |
|                             |   }],                                         | | aplican a este privilegio  |                             
|                             | "ip": "10.10.10.11",                          | |                            |
|                             | "forma_pago":"1",                             | | **Contacto:**              |
|                             | "inputCardNumber":"",                         | | **nombre_contacto:**       |
|                             | "inputMonth":"",                              | | Nombre y apellido del      |
|                             | "inputYear":"",                               | | contacto - formato         |
|                             | "inputCVV2":"",                               | | caracteres sin caracteres  |
|                             | "totalgeneral":"",                            | | especiales                 |
|                             | "inputNameCard":""                            | | **telefono_contacto:**     |
|                             | }                                             | | Número telefónico del      |
|                             |                                               | | contacto - formato         |
|                             |                                               | | númerico sin caracteres    |
|                             |                                               | | especiales                 |
|                             |                                               | | **email_contacto:**        |
|                             |                                               | | Correo electronico del     |
|                             |                                               | | contacto - formato         |
|                             |                                               | | de email                   |
|                             |                                               | |                            |
|                             |                                               | | **Beneficiarios:**         |
|                             |                                               | | **nombre:**                |
|                             |                                               | | Nombre del beneficiario    |
|                             |                                               | | formato caracteres sin     |
|                             |                                               | | caracteres especiales      |
|                             |                                               | | **apellido:**              |
|                             |                                               | | Apellido del beneficiario  |
|                             |                                               | | formato caracteres sin     |
|                             |                                               | | caracteres especiales      |
|                             |                                               | | **fechaNac:**              |
|                             |                                               | | Fecha de nacimiento del    |
|                             |                                               | | beneficiario - formato     |
|                             |                                               | | DD/MM/YYYY                 |
|                             |                                               | | **edad:**                  |
|                             |                                               | | Edad del beneficiario, en  |
|                             |                                               | | caso de ser recien nacido  |
|                             |                                               | | la edad sería cero (0)     |
|                             |                                               | | **pasaporte:**             |
|                             |                                               | | Número del documento       |
|                             |                                               | | formato caracteres         |
|                             |                                               | | **email:**                 |
|                             |                                               | | Correo electrónico del     |
|                             |                                               | | beneficiario - formato de  |
|                             |                                               | | email                      |
|                             |                                               | | **telefono:**              |
|                             |                                               | | Número telefónico del      |
|                             |                                               | | beneficiario - formato     |
|                             |                                               | | númerico sin caracteres    |
|                             |                                               | | especiales                 |
|                             |                                               | | **beneficios_adicionales:**|
|                             |                                               | | (arreglo) id de los        |
|                             |                                               | | beneficios en el servicio  |
|                             |                                               | | 'consulta_beneficios       |
|                             |                                               | | _adicionales'              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+