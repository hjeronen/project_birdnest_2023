# from https://stackoverflow.com/questions/50253173/django-how-to-make-api-calls-at-constant-intervals

import subprocess
import time
from threading import Thread, Event

event = Event()

def ping(event):
    while not event.is_set():
        print("Pinging ...") # do actual API pinging stuff here
        time.sleep(2)

t = Thread(target=ping, args=(event,))
t.start() # this will run the `ping` function in a separate thread

# now start the django server
subprocess.call(['python', 'manage.py', 'runserver'])