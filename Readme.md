Start with apt deps:
```
apt install influxdb
apt install python3
apt install python3-pip
```
Now you can start `influxdb` service:
```
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
pip3 install influxdb
```

Next, to collect data and publish it to influxdb you can run `python3 real_aqi.py` or copy `aqi.service` to `/etc/systemd/system` and enable it via 
```
sudo systemctl enable aqi.service
```

For data visualization pick some handy folder and
```
wget https://dl.influxdata.com/chronograf/releases/chronograf-1.10.0_linux_arm64.tar.gz
tar xvfz chronograf-1.10.0_linux_arm64.tar.gz
```

Launch `chronograf` and import `Home AQI.json` dashboard or check [airnow](https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf) for range mapping between ppm and AQI and create new one (`queries.sql` may be handy still)

You can install chronograf as a service via `systemctl` too by copying `chronograf.service` to `/etc/systemd/system` and adjusting as needed
