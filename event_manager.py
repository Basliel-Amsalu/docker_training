from observer import Subject

class EventManager(Subject):
    def __init__(self):
        super().__init__()

    def create_event(self, event_type, data):
        print(f"Event Created: {event_type}")
        self.notify_observers(event_type, data)
