Start with apt deps:
```
apt install influxdb
apt install python3
apt install python3-pip
apt install mosquitto mosquitto-clients
```
Now you can start both `infludb` and `mqtt` services:
```
sudo systemctl enable mosquitto.service
sudo systemctl enable influxdb.service
```

This will be required to build `RPi.GPIO` locally
```
apt install gcc
apt install libc-dev
apt install python3-dev
```
And then python deps:
```
pip3 install pms5003
pip3 install RPi.GPIO
pip3 install paho-mqtt
```


Next, you can run (manually or via cron) `real_aqi.py` to collect data and publish it to mqtt broker

---

For data visualization pick some handy folder:
```
wget https://dl.influxdata.com/chronograf/releases/chronograf-1.10.0_linux_arm64.tar.gz
tar xvfz chronograf-1.10.0_linux_arm64.tar.gz
```

Launch `chronograf` and import `Home AQI.json` dashboard or check [airnow](https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf) for range mapping between ppm and AQI and create new one (`queries.sql` may be handy still)

---

WIP: follow Home Assistant Core [installation](https://www.home-assistant.io/installation/raspberrypi/#install-home-assistant-core)