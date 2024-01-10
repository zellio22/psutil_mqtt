
import json
import time
import paho.mqtt.client as mqtt
import psutil
from datetime import datetime
import subprocess


def import_json():
    global data
    try:
        with open("config.json","r") as config :
            data=json.load(config)

        
    except Exception as e:
        #print(f"Une erreur inattendue s'est produite : {e}")  
        None
    





def cpu_freq_current():
    try:
        result = psutil.cpu_freq()[0]
        return result
    except:
        return None

def cpu_freq_min():
    try:
        result = psutil.cpu_freq()[1]
        return result
    except:
        return None

def cpu_freq_max():
    try:
        result = psutil.cpu_freq()[2]
        return result
    except:
        return None
    
def cpu_usage():
    try:
        result = psutil.cpu_percent(interval=1, percpu=False)
        return result
    except:
        return None

def cpu_temperature():
    try:
        result = psutil.sensors_temperatures()["cpu_thermal"][0][1]
        return result
    except:
        return None

def ram_usage():
    try:
        result = psutil.virtual_memory().used / (1024 ** 2)
        return result
    except:
        return None
    
def disk_usage():
    try:
        result = psutil.disk_usage("/")[3]
        return result
    except:
        return None

def time_now():
    try:
        now=datetime.now()
        result=now.strftime("%Y-%m-%d %H:%M:%S")
        return result
    except:
        return None
    
def boot_time():
    try:
        date_boot=psutil.boot_time()
        return datetime.fromtimestamp(date_boot).strftime("%Y-%m-%d %H:%M:%S")
    except: None

def up_time():
    try:
        now=datetime.now()
        date_boot=psutil.boot_time()
        delta = now - datetime.fromtimestamp(date_boot)
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_delta = f"{days} jours, {hours} heurs, {minutes} minutes, {seconds} seconds"

        return formatted_delta
    except:
        return None

def get_service_status(service_name):
    try:
        # Exécute la commande systemctl pour obtenir l'état du service
        result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True, check=True)

        # Récupère la sortie de la commande
        output = result.stdout.strip()

        # Retourne l'état du service
        return output
    except subprocess.CalledProcessError as e:
        # En cas d'erreur, imprime le message d'erreur
        #print(f"Erreur lors de l'exécution de la commande : {e}")
        return None


# Dictionnaire de fonctions
function_mapping = {
    "cpu_freq_current": cpu_freq_current,
    "cpu_freq_min": cpu_freq_min,
    "cpu_freq_max": cpu_freq_max,
    "cpu_usage": cpu_usage,
    "cpu_temperature": cpu_temperature,
    "ram_usage": ram_usage,
    "time_now":time_now,
    "boot_time":boot_time,
    "disk_usage": disk_usage,
    "up_time": up_time
    
}

def loop():
        # Le JSON fourni
    try:
        system_info_json = data["system_info"]
    except:
        #print("Pas de configuration des Info System")
        None
    
    # Dictionnaire pour stocker les résultats
    results_dict = {}
    
    # Exécution des fonctions en fonction des valeurs du JSON et stockage des résultats
    for key, value in system_info_json.items():
        if value and key in function_mapping:
            result = function_mapping[key]()
            results_dict[key] = result
    
    # Si l'option service est definit met l'etat des service a None
    try:
        service_status_json = data["service"]
        for key, value in service_status_json.items():
            results_dict[value]=None
    except:
        #print("Pas de configuaration des Services ")
        None
    
    try:
        for key, value in service_status_json.items():
            results_dict[value]=get_service_status(value)
        # Affichage du dictionnaire des résultats
    except Exception as e:
        
        print(e)
    client.publish(topic, json.dumps(results_dict, indent=4))
    print(results_dict)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connecté au broker MQTT')
    else:
        print('Échec de la connexion au broker MQTT')

# Fonction de callback lors de la publication MQTT
def on_publish(client, userdata, mid):
    print('Données publiées avec succès')

if __name__=="__main__":
    
    import_json()
    #set des variables interne
    
    broker_address = data["config"]["broker_address"] # Adresse du Broker 
    port_mqtt = data["config"]["port_mqtt"] # Port du Broker 
    topic = data["config"]["topic"]  # Sujet MQTT pour l'envoi des données
    timing=data["config"]["timing"] #Temps entre 2 publication sur le Brocker   
    
    # Configuration du client MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connexion au broker MQTT
    client.connect(broker_address, port=port_mqtt)
    
    try:
        while True:
            loop()
            time.sleep(timing)
    except KeyboardInterrupt:
        print("Ctrl+c")



#def on_connect(client, userdata, flags, rc):
#    if rc == 0:
#        print('Connecté au broker MQTT')
#    else:
#        print('Échec de la connexion au broker MQTT')
#
## Fonction de callback lors de la publication MQTT
#def on_publish(client, userdata, mid):
#    print('Données publiées avec succès')
#
## Configuration du client MQTT
#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_publish = on_publish
#
## Connexion au broker MQTT
#client.connect(broker_address, port=port_mqtt)
#
#

#
#
#try:
#    while True:
#    

#        client.publish(topic, json.dumps(system_info, indent=4))
#        time.sleep(timing)
#except KeyboardInterrupt:
#    print("Ctrl+c")
#
#    
#    
#    
#