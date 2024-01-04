
import json
import time
import paho.mqtt.client as mqtt
import json
import psutil


broker_address = '192.168.1.14'  # Adresse IP ou nom d'hôte du broker MQTT
port_mqtt = 8500  # Port du broker MQTT
topic = 'sys_info'  # Sujet MQTT pour l'envoi des données
timing=10 #Temps entre 2 publication sur le Brocker

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connecté au broker MQTT')
    else:
        print('Échec de la connexion au broker MQTT')

# Fonction de callback lors de la publication MQTT
def on_publish(client, userdata, mid):
    print('Données publiées avec succès')

# Configuration du client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connexion au broker MQTT
client.connect(broker_address, port=port_mqtt)




#print(data_unminable['data']["balance"])


try:
    while True:
    
    
        system_info={
            "cpu_freq_current":psutil.cpu_freq()[0],
            "cpu_freq_min":psutil.cpu_freq()[1],
            "cpu_freq_max":psutil.cpu_freq()[2],
            "cpu_usage":psutil.cpu_percent(interval=1, percpu=False),
            "cpu_temp":psutil.sensors_temperatures()["cpu_thermal"][0][1],
            "ram_utilization" : psutil.virtual_memory().used / (1024 ** 2),
            psutil.disk_usage("/")[3]
        }
        client.publish(topic, json.dumps(system_info, indent=4))
        time.sleep(timing)
except KeyboardInterrupt:
    print("Ctrl+c")

    
    
    
