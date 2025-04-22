# This python code is used to look for any changes on the GEEKS folder and deploy the GEEK website if it found any changes
# It check for every 10sec

import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the event is a file modification
        if event.is_directory:
            return  # Ignore directory changes
        print(f"{event.src_path} has been modified.")
        self.build_geek_site()

    def build_geek_site(self):
        # Replace this with the command you want to run
        command = "/home/blog/geeks/build_geeks_doc.sh"  # Example command
        subprocess.run(command, shell=False)  # Run the command

if __name__ == "__main__":
    path = "/home/blog/geeks"  # target directory
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)  # Monitor the directory recursively

    try:
        observer.start()
        print(f"Watching for changes in {path}...")
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
