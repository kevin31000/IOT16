# prerequisites: pip install requests
import requests
import time
import RPi.GPIO as GPIO
from seeed_dht import DHT
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Configuramos el servomotor y pulsador
# GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.IN)
#GPIO.setup(12, GPIO.OUT)
#p = GPIO.PWM(12,50)
# p.start(2.5)

# Definimos la información de la base de datos
url = "https://corlysis.com:8086/write"
# Parametros de la base de datos de corlisys
db = "YOUR_DB_NAME"
u = "token"
p = "YOUR_DB_PASSWORD"
params = {"db": db, "u": u, "p": p}

# SERVOMOTOR + PULSADOR


def Servo(p, abierto):
    input_state = GPIO.input(22)
    print('Abierto:', abierto, ' - ', 'input_state:', input_state)
    try:
        if input_state == True and abierto == False:
            print("Abriendo")
            p.ChangeDutyCycle(3.5)
            abierto = True
            input_state = False

        if input_state == True and abierto == True:
            print("Cerrando")
            p.ChangeDutyCycle(7.5)
            abierto = False
            input_state = False

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    return abierto


def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(7.5)
    abierto = False
    sensorTempHum = DHT('11', 5)
    sensorDist = GroveUltrasonicRanger(16)
    while True:
        humi, temp = sensorTempHum.read()
        print('temperatura {}C, humidity {}%'.format(temp, humi))
        # Guardamos la humedad en Corlysis
        payload = "Humedad,sensor=humedad value={}".format(humi)
        print(payload)
        r = requests.post(url, params=params, data=payload)
        print(r)

        # Guardamos la temperatura en Corlysis
        payload = "Temperatura,sensor=temperatura value={}".format(temp)
        r = requests.post(url, params=params, data=payload)

        # SENSOR DE DISTANCIA
        distance = sensorDist.get_distance()
        print('{} cm'.format(distance))
        payload = "distancia,sensor=distancia value={}".format(distance)
        r = requests.post(url, params=params, data=payload)
        if distance < 3:
            print('LLeno')
        else:
            print('Vacio')

        abierto = Servo(p, abierto)

        time.sleep(1)


if __name__ == '__main__':
    main()
