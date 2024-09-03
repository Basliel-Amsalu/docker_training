import os
from observer import Observer

class AnalyticsService(Observer):
    def __init__(self):
        self.event_counts = {
            "OrderPlaced": 0,
            "OrderShipped": 0
        }

    def update(self, event_type, data):
        if event_type in self.event_counts:
            self.event_counts[event_type] += 1
            self.update_analytics(event_type)

    def update_analytics(self, event_type):
        os.makedirs("output", exist_ok=True)
        with open("output/analytics.txt", "w") as file:
            file.write(f"Analytics Data:\n")
            for event, count in self.event_counts.items():
                file.write(f"{event}: {count}\n")
        print(f"AnalyticsService: {event_type} occurred. Updated analytics.")
