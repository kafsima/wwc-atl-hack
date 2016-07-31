import pyrebase

import sys
import time
import logging
import subprocess
import uuid
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

INSTANCE = uuid.uuid4()
MYPATH = '/Users/reese/hack/sensor-data/'
config = {
  "apiKey": "apiKey",
  "authDomain": "kafsima-48ea3.firebaseapp.com",
  "databaseURL": "https://kafsima-48ea3.firebaseio.com",
  "storageBucket": "kafsima-48ea3.appspot.com",
  "serviceAccount": "/Users/reese/hack/kafsima-PRIVATE.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


class Event(LoggingEventHandler):
    def on_modified(self, event):
        filename = event.src_path
        line = subprocess.check_output(['tail', '-1', filename])
        self.postData(line)
        # print(line)

    def postData(self, val):
        val = float(val.strip())
        sensor_name = 'sensor_' + INSTANCE.hex[0:8]

        timestamp = int(time.time())

        data = {"timestamp": timestamp, "temp": val}
        db.child("temp_sensors").child(sensor_name).push(data)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else MYPATH
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()




