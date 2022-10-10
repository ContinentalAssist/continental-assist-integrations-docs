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
|                             |                                               | | **NOTA IMPORTANTE:**       |
|                             |                                               | | Los Beneficios Adicionales |
|                             |                                               | | **'Práctica del deporte'** |
|                             |                                               | | y **'Futura mamá'**        |
|                             |                                               | | no pueden ser seleccionados|
|                             |                                               | | a la vez para un mismo     |
|                             |                                               | | beneficiario               |
|                             |                                               | |                            |
|                             |                                               | | **ip:** La dirección ip    |
|                             |                                               | | del equipo desde donde se  |
|                             |                                               | | esté haciendo la petición  |
|                             |                                               | | **forma_pago:**            |
|                             |                                               | | El valor '1'               |
|                             |                                               | | **inputCardNumber:**       |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               | | **inputMonth:**            |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               | | **inputYear:**             |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               | | **inputCVV2:**             |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               | | **totalgeneral:**          |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               | | **inputNameCard:**         |
|                             |                                               | | '' (valor vacío)           |
|                             |                                               |                              |
|                             |                                               | | **NOTA IMPORTANTE:**       |
|                             |                                               | | **En caso de rquerir el**  |
|                             |                                               | | **PLAN FAMILIAR, el**      |
|                             |                                               | | **servicio se encargará**  |
|                             |                                               | | **de realizar cada una de**|
|                             |                                               | | **las validaciones**       |
|                             |                                               | | **correspondientes a los** |
|                             |                                               | | **requerimientos mínimos** |
|                             |                                               | | **para aplicar dicho**     |
|                             |                                               | | **privilegio. por defecto**|
|                             |                                               | | **el servicio omite el**   |
|                             |                                               | | **requerimiento de PLAN**  |
|                             |                                               | | **FAMILIAR**               |
|                             |                                               |                              |
|                             |                                               |                              |
+-----------------------------+-----------------------------------------------+------------------------------+

- La estructuración del JSON antes nombrado es responsabilidad de los webmasters de los sites externos.


.. centered:: **OTROS SERVICIOS**

**Nombre del Servicio:** consulta_voucher

**Parámetros Requeridos:**

- ps
- language_id
- código

**Ejemplo:**

>>>
{
"ps":"http://prod.continentalassist.com",
"language_id":"spa",
"codigo":"CA-28L9M2-MX"
}

Al recibir los datos, este servicio evalúa el código del voucher y determina el tipo de voucher que se está consultando.

Los tipos de voucher pueden ser los siguientes:

- Voucher Estándar.
- Voucher Corporativo.
- Voucher Emisión Corporativa.
- Voucher Venta de Precompra.
- Voucher Emisión de Precompra.


**Voucher Estándar**
++++++++++++++++++++


- Conformado por código de 3 bloques separados por guiones (Ej: CA-XXXX-XX) donde la categoría no es ni “corporativo” ni “precompra”:

**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-28L9M2-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
      "voucher": "CA-28L9M2-MX",
      "id_voucher": "38646",
      "origen": "Mexico",
      "destino": "Mundial",
      "salida": "15/02/2018",
      "retorno": "15/07/2018",
      "categoria": "Larga Estadia",
      "plan": "Larga Estadía Total",
      "forma_pago": "Contado",
      "agencia": "NOMBRE DE LA AGENCIA",
      "nombre_contacto": "NOMBRE DEL CONTACTO",
      "telefono_contacto": "7124881472",
      "email_contacto": "CONTACTO@HOTMAIL.COM",
      "status": "Anulado",
      "beneficiarios": [
          {
            "nombre": "NOMBRE BENEFICIARIO 1",
            "apellido": "APELLIDOS BENEFICIARIO 1",
            "fecha_nacimiento": "03/01/1993",
            "documento": "G11764934",
            "telefono": "7222525243",
            "email": " BENEFICIARIO 1@HOTMAIL.COM",
            "voucher": "CA-28L9M2-1-MX"
          },
          {
            "nombre": "NOMBRE BENEFICIARIO 2",
            "apellido": "APELLIDOS BENEFICIARIO 2",
            "fecha_nacimiento": "03/01/1993",
            "documento": "G11764934",
            "telefono": "7222525243",
            "email": " BENEFICIARIO2@HOTMAIL.COM",
            "voucher": "CA-28L9M2-1-MX"
          }
      ]
    }
  ],
  "cantidad": 1,
  "error": false
}


- Conformado por código de 4 bloques separados por guiones (Ej: CA-XXXX-B-XX) donde la categoría no es ni “corporativo” ni “precompra”: En este caso, el bloque adicional representa el número del beneficiario, es decir que el servicio responderá con datos específicos con respecto a ese voucher, en caso de que extistan más beneficiarios asociados serían omitidos en la consulta.

**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-28L9M2-1-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
      "voucher": "CA-28L9M2-MX",
      "id_voucher": "38646",
      "origen": "Mexico",
      "destino": "Mundial",
      "salida": "15/02/2018",
      "retorno": "15/07/2018",
      "categoria": "Larga Estadia",
      "plan": "Larga Estadía Total",
      "forma_pago": "Contado",
      "agencia": "NOMBBRE DE LA AGENCIA",
      "nombre_contacto": "NOMBRE DEL CONTACTO",
      "telefono_contacto": "7124881472",
      "email_contacto": "CONTACTO@HOTMAIL.COM",
      "status": "Activo",
      "beneficiarios": [
        {
          "nombre": "NOMBRE BENEFICIARIO 1",
          "apellido": "APELLIDO BENEFICIARIO 1",
          "fecha_nacimiento": "03/01/1993",
          "documento": "G11764934",
          "telefono": "121411585",
          "email": "BENEFICIARIO1@HOTMAIL.COM",
          "voucher": "CA-28L9M2-1-MX"
        }
      ]
    }
  ],
  "cantidad": 1,
  "error": false
}

- Conformado por código de 5 bloques separados por guiones (Ej: CA-XXXX-E-B-XX). En este caso, el bloque E representa el número de la emisión y el bloque B el número del beneficiario. Este tipo de búsqueda se hacen para consultar datos directos del beneficiario de una emisión corporativa o una precompra, aún así, la respuesta del servicio sigue siendo una respuesta de voucher estándar.

**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-KCCL2M-1-1-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
    "voucher": "CA-KCCL2M-1-1-MX",
    "origen": "Mexico",
    "destino": "Mundial",
    "salida": "09/01/2018",
    "retorno": "13/01/2018",
    "categoria": "Corporativo",
    "plan": "Maximus",
    "forma_pago": "Contado",
    "agencia": "NOMBRE DE LA AGENCIA",
    "nombre_contacto": "NOMBRE DEL CONTACTO ",
    "telefono_contacto": "6141985118",
    "email_contacto": "contacto@hotmail.com",
    "beneficiarios": [
        {
          "nombre": "NOMBRE BENEFICIOARIO 1",
          "apellido": "APELLIDO BENEFICIARIO 1",
          "nacimiento": "15/12/1968",
          "edad": "49",
          "documento": "15115321",
          "telefono": "1147895616",
          "email": "beneficiario1@gmail.com",
          "voucher": "CA-KCCL2M-1-1-MX"
        }
      ]
    }
  ],
  "cantidad": 1,
  "error": false
}


**Voucher Corporativo**
+++++++++++++++++++++++


El servicio de consulta_voucher cuenta con la particularidad de responder cierto tipo de datos según el código del voucher que se esté consultando, por ejemplo: Si el código está conformado por tres bloques separados por guiones (ejemplo: CA-XXXX-XX), pero además ese código corresponde a un voucher corporativo, entonces la respuesta estará conformada por los datos de la emisión corporativa y contará con un valor **(emisiones)** compuesto por los datos de cada una de las emisiones que están asociadas a ese voucher, quien a su vez tendrá un valor con los datos de cada uno de los beneficiarios de esa emisión. Por ejemplo:

**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-KCCL2M-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
      "vocuher": "CA-KCCL2M-MX",
      "id_voucher": "37913",
      "categoria": "Corporativo",
      "plan": "Maximus",
      "forma_pago": "Contado",
      "agencia": "NOMBRE DE LA AGENCIA",
      "status": "Activo",
      "emisiones": [
        {
          "voucher": "CA-KCCL2M-1-MX",
          "id_voucher": "1291",
          "origen": "Mexico",
          "destino": "Mundial",
          "salida": "09/01/2018",
          "retorno": "13/01/2018",
          "nombre_contacto": "NOMBRE DEL CONTACTO ",
          "telefono_contacto": "11548332565",
          "email_contacto": "contacto@gmail.com",
          "beneficiarios": [
          {
            "nombre": "NOMBRE BENEFICIARIO 1",
            "apellido": "APELLIDO BENEFICIARIO 1",
            "nacimiento": "15/12/1968",
            "edad": "49",
            "documento": "x",
            "telefono": "5455125874",
            "email": "beneficiario1@hotmail.com",
            "voucher": "CA-KCCL2M-1-1-MX"
          },
          {
            "nombre": "NOMBRE BENEFICIARIO 2",
            "apellido": "APELLIDO BENEFICIARIO 2",
            "nacimiento": "15/12/1958",
            "edad": "59",
            "documento": "44651625",
            "telefono": "5455125874",
            "email": "beneficiario2@hotmail.com",
            "voucher": "CA-KCCL2M-1-2-MX"
          }
        ]
      },
      {
       "voucher": "CA-KCCL2M-2-MX",
       "id_voucher": "1467",
       "origen": "Mexico",
       "destino": "Mundial",
       "salida": "13/01/2018",
       "retorno": "14/01/2018",
       "nombre_contacto": "NOMBRE DEL CONTACTO ",
       "telefono_contacto": "6141985118",
       "email_contacto": "contacto@hotmail.com",
       "beneficiarios": [
         {
           "nombre": "NOMBRE BENEFICIARIO 1",
           "apellido": "APELLIDO BENEFICIARIO 1",
           "nacimiento": "29/12/1962",
           "edad": "55",
           "documento": ".",
           "telefono": "1255441545",
           "email": "beneficiario1@gmail.com",
           "voucher": "CA-KCCL2M-2-1-MX"
         }
       ]
      }
      ]
    }
  ],
  "cantidad": 1,
  "error": false
}


**Voucher Emisión Corporativa**
+++++++++++++++++++++++++++++++

Para esta consulta nuestro servicio se encargará de emitir los datos correspondientes a la emisión corporativa, omitiendo los datos del “voucher padre” de dicha emisión.

**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-KCCL2M-1-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
    "voucher": "CA-KCCL2M-1-MX",
    "id_voucher": "1291",
    "origen": "Mexico",
    "destino": "Mundial",
    "salida": "09/01/2018",
    "retorno": "13/01/2018",
    "categoria": "Corporativo",
    "plan": "Maximus",
    "forma_pago": "Contado",
    "agencia": "NOMBRE DE LA AGENCIA",
    "nombre_contacto": "NOMBRE DEL CONTACTO",
    "telefono_contacto": "5548569952",
    "email_contacto": "contacto@gmail.com",
    "beneficiarios": [
        {
          "nombre": "NOMBRE BENEFICIARIO 1",
          "apellido": "APELLIDO BENEFICIARIO 1",
          "nacimiento": "15/12/1968",
          "edad": "49",
          "documento": "x",
          "telefono": "5646468841",
          "email": "beneficiario1@gmail.com",
          "voucher": "CA-KCCL2M-1-1-MX"
        }
      ]
    }
  ],
  "cantidad": 1,
  "error": false
}


**Voucher Venta de Precompra**
++++++++++++++++++++++++++++++


**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-IBJ6B3-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
      "vocuher": "CA-IBJ6B3-MX",
      "id_voucher": "26614",
      "categoria": "Precompra",
      "plan": "Maximus",
      "forma_pago": "Contado",
      "agencia": "NOMBRE DE LA AGENCIA",
      "status": "Activo",
      "emisiones": [
        {
          "voucher": "CA-ELC00E-MX",
          "id": "31096",
          "origen": "Mexico",
          "destino": "Mundial",
          "salida": "01/09/2017",
          "retorno": "26/09/2017",
          "categoria": "Precompra",
          "plan": "Maximus",
          "forma_pago": "Contado",
          "agencia": "NOMBRE DE LA AGENCIA",
          "nombre_contacto": "NOMBRE DEL CONTACTO",
          "telefono_contacto": "55215859",
          "email_contacto": "",
          "beneficiarios": [
            {
              "nombre": "NOMBRE BENEFICIARIO 1",
              "apellido": "APELLIDO BENEFICIARIO 1",
              "nacimiento": "24/10/1950",
              "edad": "67",
              "documento": "G55485752",
              "telefono": "55215859",
              "email": "BENEFICIARIO1@GMAIL.MX",
              "voucher": "CA-ELC00E-1-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 2",
              "apellido": " APELLIDO BENEFICIARIO 2",
              "nacimiento": "15/04/1937",
              "edad": "81",
              "documento": "G25708511",
              "telefono": "55215859",
              "email": "BENEFICIARIO2@GMAIL.MX",
              "voucher": "CA-ELC00E-2-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 3",
              "apellido": "APELLIDO BENEFICIARIO 3",
              "nacimiento": "24/08/1958",
              "edad": "59",
              "documento": "G544488777",
              "telefono": "55215859",
              "email": "BENEFICIARIO3@GMAIL.MX",
              "voucher": "CA-ELC00E-3-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 4",
              "apellido": "APELLIDO BENEFICIARIO 4",
              "nacimiento": "03/04/1956",
              "edad": "62",
              "documento": "G8889654",
              "telefono": "55215859",
              "email": "BEN4@GMAIL.MX",
              "voucher": "CA-ELC00E-4-MX"
            }
          ]
        },
        {
          "voucher": "CA-4CEKJB-MX",
          "id": "33516",
          "origen": "Mexico",
          "destino": "Mundial",
          "salida": "14/10/2017",
          "retorno": "24/10/2017",
          "categoria": "Precompra",
          "plan": "Maximus",
          "forma_pago": "Contado",
          "agencia": "NOMBRE DE LA AGENCIA",
          "nombre_contacto": "NOMBRE CONTACTO",
          "telefono_contacto": "5554888787",
          "email_contacto": "",
          "beneficiarios": [
            {
              "nombre": " NOMBRE BENEFICIARIO 1",
              "apellido": "APELLIDO BENEFICIARIO 1",
              "nacimiento": "15/06/1951",
              "edad": "66",
              "documento": "G888223123",
              "telefono": "55215859",
              "email": "BENEFICIARIO1@GMAIL.MX",
              "voucher": "CA-4CEKJB-1-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 2",
              "apellido": "APELLIDO BENEFICIARIO 2",
              "nacimiento": "15/05/1959",
              "edad": "59",
              "documento": "G66335241",
              "telefono": "55215859",
              "email": "BENEFICIARIO2@GMAIL.MX",
              "voucher": "CA-4CEKJB-2-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 3",
              "apellido": "APELLIDO BENEFICIARIO 3",
              "nacimiento": "28/03/1967",
              "edad": "51",
              "documento": "G777845444",
              "telefono": "55215859",
              "email": "BEBENFICIARIO3@GMAIL.MX",
              "voucher": "CA-4CEKJB-3-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 4",
              "apellido": "APELLIDO BENEFICIARIO 4",
              "nacimiento": "25/10/1993",
              "edad": "24",
              "documento": "G555564565",
              "telefono": "55215859",
              "email": "BENEFICIARIO4@GMAIL.MX",
              "voucher": "CA-4CEKJB-4-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 5",
              "apellido": "APELLIDO BENEFICIARIO 5",
              "nacimiento": "05/08/1951",
              "edad": "66",
              "documento": "G777747474",
              "telefono": "55215859",
              "email": "BENEFICIARIO5@GMAIL.MX",
              "voucher": "CA-4CEKJB-5-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 6",
              "apellido": "APELLIDO BENEFICIARIO 6",
              "nacimiento": "22/09/1960",
              "edad": "57",
              "documento": "G2212121",
              "telefono": "55215859",
              "email": "BENEFICIARIO6@GMAIL.MX",
              "voucher": "CA-4CEKJB-6-MX"
            }
          ]
        },
        {
          "voucher": "CA-7C1L86-MX",
          "id": "33525",
          "origen": "Mexico",
          "destino": "Mundial",
          "salida": "14/10/2017",
          "retorno": "24/10/2017",
          "categoria": "Precompra",
          "plan": "Maximus",
          "forma_pago": "Contado",
          "agencia": "NOMBRE DE LA AGENCIA",
          "nombre_contacto": "NOMBRE DEL CONTACTO",
          "telefono_contacto": "55215859",
          "email_contacto": "",
          "beneficiarios": [
            {
              "nombre": " NOMBRE BENEFICIARIO 1",
              "apellido": "APELLIDO BENEFICIARIO 1",
              "nacimiento": "14/05/1953",
              "edad": "65",
              "documento": "G19301617",
              "telefono": "55215859",
              "email": "BENEFICIARIO1@GMAIL.MX",
              "voucher": "CA-7C1L86-1-MX"
            },
            {
              "nombre": "NOMBRE BENEFICIARIO 1",
              "apellido": "APELLIDO BENEFICIARIO 1",
              "nacimiento": "02/10/1947",
              "edad": "70",
              "documento": "G17737367",
              "telefono": "55215859",
              "email": "BENEFICIARIO1@GMAIL.MX",
              "voucher": "CA-7C1L86-2-MX"
            },
            {
              "nombre": "NOMBRE BENEFICIARIO 2",
              "apellido": "APELLIDO BENEFICIARIO 2",
              "nacimiento": "20/11/1953",
              "edad": "64",
              "documento": "G999656564",
              "telefono": "55215859",
              "email": "BENEFICIARIO2@GMAIL.MX",
              "voucher": "CA-7C1L86-3-MX"
            },
            {
              "nombre": "NOMBRE BENEFICIARIO 3",
              "apellido": "APELLIDO BENEFICIARIO 3",
              "nacimiento": "06/01/1951",
              "edad": "67",
              "documento": "G1121235",
              "telefono": "55215859",
              "email": "BENEFICIARIO3@GMAIL.MX",
              "voucher": "CA-7C1L86-4-MX"
            },
            {
              "nombre": "NOMBRE BENEFICIARIO 4",
              "apellido": "APELLIDO BENEFICIARIO 4",
              "nacimiento": "15/07/1961",
              "edad": "56",
              "documento": "G015232",
              "telefono": "55215859",
              "email": "BENEFICIARIO4@GMAIL.MX",
              "voucher": "CA-7C1L86-5-MX"
            },
            {
              "nombre": "NOMBRE BENEFICIARIO 5",
              "apellido": "APELLIDO BENEFICIARIO 5",
              "nacimiento": "02/09/1940",
              "edad": "77",
              "documento": "YB09052",
              "telefono": "55215859",
              "email": "BENEFICIARIO5@GMAIL.MX",
              "voucher": "CA-7C1L86-6-MX"
            },
            {
              "nombre": " NOMBRE BENEFICIARIO 6",
              "apellido": " APELLIDO BENEFICIARIO 6",
              "nacimiento": "24/01/1945",
              "edad": "73",
              "documento": "G267311",
              "telefono": "55215859",
              "email": "BENEFICIARIO@GMAIL.MX",
              "voucher": "CA-7C1L86-7-MX"
            }
          ]
        },
        {
          "voucher": "CA-5FKAJD-MX",
          "id": "33617",
          "origen": "Mexico",
          "destino": "Mundial",
          "salida": "14/10/2017",
          "retorno": "24/10/2017",
          "categoria": "Precompra",
          "plan": "Maximus",
          "forma_pago": "Contado",
          "agencia": "NOMBRE DE LA AGENCIA",
          "nombre_contacto": "NOMBRE DEL CONTACTO",
          "telefono_contacto": "55215859",
          "email_contacto": "CONTACTO@GMAIL.MX",
          "beneficiarios": [
            {
              "nombre": " NOMBRE BENEFICIARIO 1",
              "apellido": " APELLIDO BENEFICIARIO 1",
              "nacimiento": "02/11/1968",
              "edad": "49",
              "documento": "G267996",
              "telefono": "55215859",
              "email": "BENEFICIARIO@GMAIL.MX",
              "voucher": "CA-5FKAJD-1-MX"
            }
          ]
        }
      ]
    }
  ],
  "cantidad": 1,
  "error": false 
}


**Voucher Emisión de Precompra**
++++++++++++++++++++++++++++++++


**Petición:**

>>>
{
  "ps":"http://prod.continentalassist.com",
  "language_id":"spa",
  "codigo":"CA-ELC00E-MX"
}

**Respuesta:**

>>>
{
  "resultado": [
    {
    "voucher": "CA-ELC00E-MX",
    "id_voucher": "31096",
    "origen": "Mexico",
    "destino": "Mundial",
    "salida": "01/09/2017",
    "retorno": "26/09/2017",
    "categoria": "Precompra",
    "plan": "Maximus",
    "forma_pago": "Contado",
    "agencia": "NOMBRE DE LA AGENCIA",
    "nombre_contacto": "NOMBRE CONTACTO",
    "telefono_contacto": "55215859",
    "email_contacto": "",
    "status": "Activo",
    "beneficiarios": [
      {
        "nombre": " NOMBRE BENEFICIARIO 1",
        "apellido": "APELLIDO BENEFICIARIO 1",
        "fecha_nacimiento": "24/10/1950",
        "documento": "G08532627",
        "telefono": "55215859",
        "email": "BENEFICIARIO1@CENTRODEPEREGRINACIONES.MX",
        "voucher": "CA-ELC00E-1-MX"
      },
      {
        "nombre": " NOMBRE BENEFICIARIO 2",
        "apellido": " APELLIDO BENEFICIARIO 2",
        "fecha_nacimiento": "15/04/1937",
        "documento": "G25708511",
        "telefono": "55215859",
        "email": " BENEFICIARIO2@CENTRODEPEREGRINACIONES.MX",
        "voucher": "CA-ELC00E-2-MX"
      },
      {
        "nombre": " NOMBRE BENEFICIARIO 3",
        "apellido": " APELLIDO BENEFICIARIO 3",
        "fecha_nacimiento": "24/08/1958",
        "documento": "G11381859",
        "telefono": "55215859",
        "email": " BENEFICIARIO3@CENTRODEPEREGRINACIONES.MX",
        "voucher": "CA-ELC00E-3-MX"
      },
      {
        "nombre": "NOMBRE BENEFICIARIO 4",
        "apellido": " APELLIDO BENEFICIARIO 4",
        "fecha_nacimiento": "03/04/1956",
        "documento": "G09009213",
        "telefono": "55215859",
        "email": " BENEFICIARIO4@CENTRODEPEREGRINACIONES.MX",
        "voucher": "CA-ELC00E-4-MX"
      }
      ]
    }
  ],
  "cantidad": 1,
  "error": false 
}


**Nombre del Servicio:** consulta_planes_grupal
+++++++++++++++++++++++++++++++++++++++++++++++

**Parámetros Requeridos:**

- ps
- dias
- edades
- id_categoria
- id_destino
- familiar

**Ejemplo:**

>>>
{
  "ps":"prod.continentalassist.com",
  "dias":5,
  "edades":[14,30,70],
  "id_categoria":24,
  "id_destino":2,
  "familiar": 1
}

Al recibir los datos, este servicio evalúa el parámetro “edades” y los valores de las edades máximas de la categoría seleccionada, para así determinar cuántos menores, cuántos adultos y cuántas personas de tercera edad, comprenden dicho campo. 

Se debe tomar en cuenta que si alguna de las edades está por encima de los valores de la edad máxima de la categoría seleccionada, el servicio simplemente responderá con valores vacíos:

>>>
{
  "resultado": [],
  "cantidad": 0,
  "error": false
}

ya que **el valor de las edades máximas no depende únicamente de la categoría sino también de cada uno de los planes que conforman dicha categoría.**

Así mismo, localiza los planes cuyos mínimos y máximos de días correspondan con los que tengan asignados y que obviamente pertenezcan a la categoría seleccionada.

Tomando en cuenta estas condiciones, el servicio se encargará de calcular el precio grupal del plan, basándose en las reglas de negocio del mismo, los incrementos por edades, los descuentos familiares y la cantidad de días en el parámetro “dias”.

En caso de que el parámetro “familiar” tenga valor 1, que la categoría acepte el descuento de Plan Familiar y que las edades correspondan a las edades permitidas para dicho beneficio, el servicio se encargará de realizar los respectivos cálculos, para así emitir una respuesta basada en el descuento de Plan Familiar.


**Respuesta:**

>>>
{
  "resultado": [
    {
      "id": "21",
      "valor": "21",
      "nombre": "Traveler",
      "precio": "348.00",
      "precio_adulto_mayor": "522.00",
      "moneda": "USD",
      "edad_maxima_sin_incremento": "70",
      "acepta_pago_tdc": "SI",
      "precio_grupal": "870.00"
    }
  ],
  “cantidad”: 1,
  “error”: false
}


