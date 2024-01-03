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
##Instalation des dependances
Installez les dépendances requises avec la commande suivante :
```bach
    pip install -r requirement.txt
```

## Configuration 

```python
    broker_address = '192.168.1.14'  # Adresse IP ou nom d'hôte du broker MQTT
    port_mqtt = 8500  # Port du broker MQTT
    topic = 'sys_info'  # Sujet MQTT pour l'envoi des données
    timing=10 #Temps entre 2 publication sur le Brocker
```


## Execution 

Exécutez le script avec la commande suivante :
```bash 
python3 ./main.py
```
