# Sys_info
Le script suivant permet de publier sur votre broker MQTT les informations suivantes :
    "cpu_freq_current": 
    "cpu_freq_min": 
    "cpu_freq_max": 
    "cpu_usage": 
    "cpu_temp": 
    "ram_utilization": 

## Instalation 
Clônez le dépôt avec la commande suivante :

```bach
git clone https://github.com/zellio22/psutil_mqtt
```

```bash 
cd ./psutil_mqtt/

```
## Instalation des dependances

Installez les dépendances requises avec les commande suivante :

```bach
pip install pypi-json
```
```bach
pip install psutil
```
```bach
pip install paho-mqtt
```
Ou 
```bash
pip install -r requirement.txt
```
## Configuration 

```python
broker_address = '127.0.0.1'  # Adresse IP ou nom d'hôte du broker MQTT 127.0.0.1 si le brocker est sur la meme machine 
port_mqtt = 1883  # Port du broker MQTT 1883 port MQTT par defaut 
topic = 'sys_info'  # Sujet MQTT pour l'envoi des données
timing=10 #Temps entre 2 publication sur le Brocker
```


## Execution 

Exécutez le script avec la commande suivante :
```bash 
python3 ./main.py
```
## Screen 
![Mqtt](./images/mqtt.png)
