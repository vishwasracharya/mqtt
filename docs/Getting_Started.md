# MQTT  (Message Queuing Telemetry Transport)

Installation Guide (Ubuntu): https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/

Subscribe & Publisher Command With Authentication:
```bash
mosquitto_sub -u vishwas_acharya -P MY_PASSWORD -t “home/lights/sitting_room”
```

```bash
mosquitto_pub -u vishwas_acharya -P MY_PASSWORD -t “home/lights/sitting_room” -m “ON”
```