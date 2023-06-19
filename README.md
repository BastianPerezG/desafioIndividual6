# desafioIndividual6
En este repositorio estará el desafío individual 6 del Bootcamp FullStack Python, el cual consiste en la creación de usuarios de manera dinámica, donde ellos también puedan escoger a que grupo pertenecer, así tener permisos diferenciados

# desafioIndividual6
En este repositorio estará el desafío individual 6 del Bootcamp FullStack Python, el cual consiste en la creación de usuarios de manera dinámica, donde ellos también puedan escoger a que grupo pertenecer, así tener permisos diferenciados

Documentación de uso.

-Descargar el Zip desde el github -Descomprimir y abrir a través de su editor de código preferido -Ingresar a la carpeta sistemaVentas, abrir un terminal y correr el comando python manage.py runserver -Luego ingresar desde un navegador web al localhost http://127.0.0.1:8000/ -Una vez dentro debería poder visualizar la landing page.

Proceso de autenticación

En la landing page a un navbar con el botón de login, dentro de esa página usted podrá ingresar a la aplicación con los siguientes usuarios (por default):

ejohnson odavis awilson

y la clave de todos estas cuentas es hola.123

Al autenticarse se redirigirá a la landing page pero en el navbar aparecerá un nueva opción en el navbar llamada PaginaRestringida, esa página solo puede ser accedida una vez logueado. En esa página podrá ver la bienvenida personalizada al usuario y además del catálogo de productos.


IMPLEMENTACION DESAFIO 6

En esta versión del proyecto se modificó el formulario de usuarios anterior y ahora se agregó la opción de creación de usuario dinámica, el cual puede ser accedida a través del enlace Registrarse que se encuentra en el navbar de la landing page.

Dentro del formulario hay una opción para escoger grupos, en este proyecto existen solo 2 que son trabajadores y clientes.

Al crear una cuenta de trabajadores tendrá acceso a la opción de registro en su totalidad además de una opción (solo representativa) de un permiso que especial que se creó para el grupo que se llama "permiso exclusivo trabajadores".

Por otro lado el grupo de clientes tiene acceso solo a agregar y ver el formulario, además de su respectivo permiso especial que se llama "permiso exclisuvo clientes"

Para salir del programa solo cierre el servidor aplicando ctrl + c en el terminal donde lo tenía funcionando.
