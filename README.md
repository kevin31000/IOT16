# IOT16

## Descripcion
Nuestra idea de proyecto de Sistema IoT se trata de crear un contenedor de basura de calle
inteligente, que dé solución a algunos de los problemas más comunes que se pueden
apreciar en este ámbito.

Nuestra propuesta en cuanto al problema de abrir el contenedor, es mantener el sistema
tradicional, pero añadir un sistema de lector de tarjetas NFC para que todo aquel que quiera
o lo necesite, pueda tener esta solución, donde la tapa se abrirá automáticamente al pasar
la tarjeta. Para solucionar el problema del exceso de capacidad en los contenedores,
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

## 📋 Pre-requisitos 📋
* Python 3
* Raspberry Pi con Linux
* Grove - Temperature and Humidity Sensor(DHT11)
* Grove - Ultrasonic Ranger
* RFID sensor (mfrc522)

## 🚀 Comenzando 🚀
Para obtener una copia local del proyecto en funcionamiento para propósitos de desarrollo y pruebas 
es necesario descargarse este repositorio e importarlo a un IDE de programación compatible con los requisitos previamente nombrados.

## 🔧 Instalación y ejecución 🔧
Para clonar el proyecto usaremos el enlace de este repositorio, y usaremos el siguiente comando.
```
git clone https://github.com/kevin31000/IOT16 
````
Para poder ejecutarlo, entramos a la carpeta que contiene el proyecto mediante la Raspberry Pi.
```
cd IOT16 
````
Instalamos las dependencias necesarias para ejecutar de manera satisfactoria el proyecto.
```
pip install -r requirements.txt 
````
Y ejecutamos el siguiente comando, que hace referencia al archivo Python que contiene el código necesario para el correcto funcionamiento del sistema.
```
python3 Main.py
````
### 🛠️ Herramientas utilizadas 🛠️
*Raspberry

### ✒️ Autores ✒️

* [Kevin Arnaiz] (https://github.com/kevin31000)
* [Asier Goirigolzarri] (https://github.com/AsierGoiri)
* [Sergio Cogollos] (https://github.com/SergioCo99)
