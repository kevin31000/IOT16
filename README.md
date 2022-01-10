# IOT16

## Descripcion
Nuestra idea de proyecto de Sistema IoT se trata de crear un contenedor de basura de calle
inteligente, que dé solución a algunos de los problemas más comunes que se pueden
apreciar en este ámbito.

Nuestra propuesta en cuanto al problema de abrir el contenedor, es mantener el sistema
tradicional, pero añadir un botón o pulsador, para que todo aquel que quiera
o lo necesite pueda tener esta solución, donde la tapa se abrirá automáticamente al pulsar dicho botón.
Para solucionar el problema del exceso de capacidad en los contenedores,
queremos implementar unos sensores, de ultrasonido por ejemplo, los cuales están
ubicados en la tapa superior del contenedor, apuntando hacia abajo, de esta manera el
sensor recoge la información de la distancia a la que rebota el ultrasonido, marcando asi
como lleno cuando la distancia sea mínima.
Para minimizar el efecto de incendios en contenedores, tenemos pensado instalar dos
sensores, uno de temperatura y otro de gas, y en caso de superarse los niveles normales
establecidos de estos factores, daría un aviso a las autoridades.
De esta manera, estamos seguros de que nuestro sistema es muchísimo más beneficioso
que el actual para la sociedad, ya que elimina algunos de los problemas que se pueden ver
hoy en día.

## 📋 Hardware utilizado 📋
* Raspberry Pi con Linux
* Grove - Temperature and Humidity Sensor(DHT11)
* Grove - Ultrasonic Ranger
* Grove - Button
* Grove - Servo

## 🚀 Comenzando 🚀
Para obtener una copia local del proyecto en funcionamiento para propósitos de desarrollo y pruebas 
es necesario descargarse este repositorio e importarlo a un IDE de programación compatible con los requisitos previamente nombrados.

En caso de querer ver la presentación y un video del prototipo, acceder a la siguiente url:
```
https://docs.google.com/presentation/d/1IM7abmOL6J3qKKMy9zRbdOyrKys8xs94jNL5S_qJIW0/edit?usp=sharing
````

## 🔧 Instalación y ejecución 🔧
Para clonar el proyecto usaremos el enlace de este repositorio, y usaremos el siguiente comando.
```
git clone https://github.com/kevin31000/IOT16 
````
Para poder ejecutarlo, entramos a la carpeta que contiene el proyecto mediante la Raspberry Pi.
```
cd IOT16 
````
Y ejecutamos el siguiente comando, que hace referencia al archivo Python que contiene el código necesario para el correcto funcionamiento del sistema. Es neceario tener instalado python en su versión 3 para su ejecución.
```
python3 Main.py
````
Una vez ejecutado por consola irá apareciendo un log mostrando los distintos datos de los sensores. Además, todos esos datos están siendo enviados a la base de datos creada en Corlysis. Para su vinculación, es necesario que el nombre de la DB, el usuario y la password coincidan con los datos añadidos en el fichero Main.py. En caso de querer recrear el proyecto, se deberá crear una base de datos en Corlysis y copiar los datos en el archivo de python.
```
Web de Corlysis: https://corlysis.com/
````
Por último, para poder analizar los datos hacemos uso de Grafana. Gracias a esta herramienta podemos analizar los datos obtenidos de los sensores cada muy pocos segundos y registrar la actividad. Además, al hacer uso de gráficas es muy sencillo analizar la información obtenida y crear alertas personalizadas en el momento que los valores en este caso lleguen a estados de peligro: mucho calor por fuego, contenedor lleno...

### 🛠️ Herramientas utilizadas 🛠️
* Putty
* Grafana
* Corlysis

### ✒️ Autores ✒️

* [Kevin Arnaiz] (https://github.com/kevin31000)
* [Asier Goirigolzarri] (https://github.com/AsierGoiri)
* [Sergio Cogollos] (https://github.com/SergioCo99)
