# mqtt-rest

Export JSON formatted mqtt messages to any REST API

## Build docker image 
```
docker build -t mqtt-rest .
```

## Configure 
Edit `.env` file
```
API_URL=https://hookb.in/wNxZwDP9NkhqJmrrJ06p
MQTT_SERVER=test.mosquitto.org
MQTT_SERVER_PORT=1883
MQTT_TOPIC=/test/#
```

## Run 
```
docker run -it --env-file .env mqtt-rest
```

## License
[MIT](https://choosealicense.com/licenses/mit/)