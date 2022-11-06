Start with apt deps:
```
apt install influxdb
apt install python3
apt install python3-pip
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
```

Dont forget to add `real_aqi.py` to cron

For UI pick some handy folder:
```
wget https://dl.influxdata.com/chronograf/releases/chronograf-1.10.0_linux_arm64.tar.gz
tar xvfz chronograf-1.10.0_linux_arm64.tar.gz
```

When building Dashboard check [airnow](https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf) for range mapping between ppm and AQI

![](./Screenshot.png)
