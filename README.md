### TAREA 1

### README
- **Descripción**: La aplicación MyTask es una herramienta de gestión de tareas que permite a los usuarios organizar y controlar sus actividades personales. Los usuarios pueden iniciar sesión o registrarse, crear tareas, editarlas, eliminarlas, cambiar su estado, y realizar búsquedas. Además, cuenta con opciones para ver detalles específicos de cada tarea, visualizar tareas completadas y registrar todas las acciones en un archivo de auditoría (log). Las tareas y los usuarios se almacenan en archivos JSON, permitiendo persistencia de datos entre sesiones.
- **Instalación**: Para instalar la aplicación MyTask, siga los siguientes pasos:
Descargue o clone el repositorio desde GitHub.
Abra el proyecto en su editor de texto preferido o acceda al directorio del proyecto desde la consola.
Asegúrese de tener Python instalado en su sistema.
Ejecute el archivo main.py de la carpeta "MyTask v4" utilizando el comando python main.py desde la consola para iniciar la aplicación.
No se requieren dependencias externas adicionales, ya que el proyecto funciona con módulos estándar de Python.
- **Uso**: La aplicación MyTask se utiliza de forma sencilla a través de la consola. Siga los pasos a continuación para interactuar con la aplicación:
Al iniciar la aplicación, se le presentarán las opciones para registrarse o iniciar sesión. Utilice el teclado para seleccionar la opción correspondiente.
Después de iniciar sesión, tendrá acceso al menú principal.
Desde el menú principal, podrá:
Revisar sus tareas existentes.
Crear nuevas tareas si no tiene ninguna registrada.
Filtrar, editar, eliminar o consultar el detalle de sus tareas.
Para cerrar la aplicación, seleccione la opción correspondiente en el menú principal.
Todas las interacciones se realizan mediante la selección de opciones utilizando el teclado.
- **Contribuciones**: Para contribuir por favor ponerse en contacto con nosotros. Revisar sección Contacto.
- **Licencia**: Este proyecto se distribuye bajo la licencia MIT. Para más detalles sobre los términos de la licencia, consulte el archivo LICENSE en el repositorio.
- **Contacto**: Para cualquier consulta o sugerencia, puede contactarnos a través de los siguientes correos electrónicos:
Rodrigo Vera: rodrigo.verav@usm.cl
Diego Morales: diegomoralesar@usm.cl


### SECCIÓN ENTREGABLE:

- **¿Cómo especificarías mejor el requerimiento?**
  - Requerimiento: El sistema debe permitir a los usuarios autenticarse, crear, consultar, editar y eliminar sus tareas, asegurando que cada usuario solo pueda ver y manipular sus propias tareas.
  - El requerimiento debe incluir:
    - Funcionalidad de autenticación: Permite iniciar sesión o registrarse.
    - Gestión de tareas: Crear, consultar, editar, eliminar y cambiar el estado de las tareas.
    - Privacidad: Las tareas deben estar asociadas a un usuario, y solo el usuario autenticado debe tener acceso a ellas.
- **¿Cómo asegurarías que el programa cumpla el requerimiento?**
- **Organización, explicar cómo se organizó el proyecto y el flujo de trabajo de éste.**
  - La organización del proyecto siguió una estructura clara y colaborativa:
  - Organización por módulos: El proyecto se dividió en tres módulos, cada uno con responsabilidades específicas: autenticación de usuarios (usuarios.py), gestión de tareas (tareas.py), e interfaz principal (main.py). Cada módulo se desarrolló de forma independiente y luego se integró.
  - Colaboración en equipo: Utilizamos GitHub para mantener el código, lo que permitió la colaboración fluida entre los miembros del equipo. Ambos compañeros trabajamos en dos ramas de forma independiente y, luego de que cada uno verificara el trabajo del otro, realizábamos el merge a la rama principal mediante pull requests y commits frecuentes. Esto aseguró un flujo de trabajo organizado y controlado.
  - Flujo de trabajo ágil:Utilizamos WhatsApp, Discord y Slack para mantener la comunicación en tiempo real y actualizaciones del progreso.
- **Incluir evidencia de flujo de trabajo y configuraciones realizadas (Imágenes de pantalla).**
  - Revisar archivo de imagenes dentro del repositorio. 
- **Problemas encontrados y como se solucionaron.**
  -  El principal problema que enfrentamos fue la manera de manejar los datos. Inicialmente, teníamos pensado utilizar MongoDB, pero con el avance del proyecto, nos dimos cuenta de que añadir una base de datos compleja como MongoDB era innecesario para los requisitos del proyecto. Finalmente, decidimos simplificar el proceso utilizando archivos .json para almacenar los datos de las tareas y usuarios, lo que facilitó la implementación y evitó complicaciones adicionales.
