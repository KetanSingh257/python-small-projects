import time
from plyer import notification

while True:
    notification.notify()
    title=("Water Reminder")
    message=("Time to drink water! Stay hydrated.")
    timeout=10
    
    
    time.sleep(10)