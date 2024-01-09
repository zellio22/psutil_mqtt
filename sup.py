import subprocess

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
        print(f"Erreur lors de l'exécution de la commande : {e}")
        return None

# Exemple d'utilisation
service_name = 'apache2'
status = get_service_status(service_name)

if status is not None:
    print(f"L'état du service {service_name} est : {status}")