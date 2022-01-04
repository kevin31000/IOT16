# prerequisites: pip install requests
import requests
import time
from seeed_dht import DHT
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Definimos la información de la base de datos
url = "https://corlysis.com:8086/write"
# Parametros de la base de datos de corlisys
db = "Corlysis"
u = "token"
p = "040427a44a4f58bc52576e37e650dbf0"
params = {"db": db, "u": u, "p": p}


def main():
	sensorTempHum = DHT('11',5)
	sensorDist = GroveUltrasonicRanger(16)

	while True:
		humi, temp = sensorTempHum.read()
		print('temperatura {}C, humidity {}%'.format(temp, humi))
		#Guardamos la humedad en Corlysis
		payload = "Humedad,sensor=humedad value={}".format(humi)
		print(payload)
		r = requests.post(url, params=params, data=payload)
		print(r)
		#Guardamos la temperatura en Corlysis
		payload = "Temperatura,sensor=temperatura value={}".format(temp)
		r = requests.post(url, params=params, data=payload)

		#SENSOR DE DISTANCIA
		distance = sensorDist.get_distance()
		print('{} cm'.format(distance))
		payload = "distancia,sensor=distancia value={}".format(distance)
		r = requests.post(url, params=params, data=payload)
		if distance < 100:
			print('LLeno')
		else:
			print('Vacio')
		time.sleep(1)


if __name__ == '__main__':
	main()
