from influxdb import InfluxDBClient
import time
import random
from pms5003 import PMS5003
from paho.mqtt import client as mqtt_client

counter = 0

def connect_mqtt():
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    
    def cb(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = cb
    client.connect("localhost", 1883)
    return client

def connect_influxdb():
  client = InfluxDBClient(host="localhost", port=8086)
  client.create_database("aqi_real")
  client.switch_database("aqi_real")
  return client

def connect_pms5003():
  pms5003 = PMS5003(
      device='/dev/ttyAMA0',
      baudrate=9600,
      pin_enable=22,
      pin_reset=27
  )
  return pms5003


def init():
  return (connect_influxdb(), connect_mqtt(), connect_pms5003())

def tick(influxdb, mqtt, pms5003):
  global counter
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
    influxdb.write_points(points)
    
    if data.pm_ug_per_m3(2.5) >= 10:
      mqtt.publish("/home/pm", "ON")
    elif data.pm_ug_per_m3(2.5) <= 5:
      mqtt.publish("/home/pm", "OFF")
    
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
    influxdb.write_points(error)

if __name__ == '__main__':
  (influxdb, mqtt, pms5003) = init()
  while True: tick(influxdb, mqtt, pms5003)
