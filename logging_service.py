import os
from observer import Observer

class LoggingService(Observer):
    def update(self, event_type, data):
        log_message = ""
        if event_type == "OrderPlaced":
            log_message = f"OrderPlaced event: {data}"
        elif event_type == "OrderShipped":
            log_message = f"OrderShipped event: {data}"

        self.log_event(log_message)

    def log_event(self, log_message):
        os.makedirs("output", exist_ok=True)
        with open("output/events.log", "a") as file:
            file.write(log_message + "\n")
        print(f"LoggingService: {log_message}")
