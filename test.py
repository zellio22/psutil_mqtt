import json
try:
    with open("config.json","r") as config :
        data=json.load(config)
        
    print(data["config"]["topic"])
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")  
    
