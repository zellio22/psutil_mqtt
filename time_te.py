import psutil
from datetime import datetime, timedelta

now=datetime.now()
print("now = ",now.strftime("%Y-%m-%d %H:%M:%S"))

date_boot=psutil.boot_time()
print("boot = ",datetime.fromtimestamp(date_boot).strftime("%Y-%m-%d %H:%M:%S"))

# Calculer la différence entre les deux timestamps
delta = now - datetime.fromtimestamp(date_boot)

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Formatez la différence de temps en une chaîne sans microsecondes
formatted_delta = f"{days} jours, {hours} heurs, {minutes} minutes, {seconds} seconds"

print("Delta =", formatted_delta)