from influxdb import InfluxDBClient
import time
from pms5003 import PMS5003

client = None
pms5003 = None
counter = 0

def init():
	global client, pms5003, counter
	client = InfluxDBClient(host="localhost", port=8086)
	client.create_database("aqi_real")
	client.switch_database("aqi_real")

	pms5003 = PMS5003(
	    device='/dev/ttyAMA0',
	    baudrate=9600,
	    pin_enable=22,
	    pin_reset=27
	)

	counter = 0


def tick():
	global client, pms5003, counter
	try:
		data = pms5003.read()
		points = [
		  {
		    "measurement" : "aqi",
		    "fields": {
		      "pm1": data.pm_ug_per_m3(1.0),
		      "pm2.5": data.pm_ug_per_m3(2.5),
		      "pm10": data.pm_ug_per_m3(10),
		    }
		  }
		]
		client.write_points(points)
		if counter > 60:
			counter = 0
			pms5003.reset()
		else:
			counter = counter + 1
		time.sleep(10)
	except Exception as err:
		error = [
	          {
	            "measurement" : "aqi_error",
	            "fields": {
        	      "reason": str(err),
	            }
	          }
		]
		client.write_points(error)
		init() # reinit and pray


if __name__ == '__main__':
	init()
	while True: tick()
