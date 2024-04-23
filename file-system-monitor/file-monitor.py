import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        log_message = f"Event type: {event.event_type} | Path: {event.src_path}"
        logger.info(log_message)

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s',
                    filename='event_log.txt', filemode='a')
logger = logging.getLogger()

# Define the directory to monitor
path = "D:\Program Files (x86)"  # Update with the desired directory path

# Create an instance of the event handler
event_handler = MyEventHandler()

# Create an observer and start monitoring the directory
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    # Keep the program running until interrupted
    while True:
        pass
except KeyboardInterrupt:
    # Stop the observer if interrupted
    observer.stop()

# Wait for the observer to complete
observer.join()
