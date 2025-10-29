# main.py
import time
from plyer import notification

print("it is... is it run, means, or, uh... It should")
while True:
    time.sleep(30*60) # Wait 30 minutes
    notification.notify(title="Drink some water!", message="You need to drink some water!")
    print("Notifications.")
    time.sleep(5)
