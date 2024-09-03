import os
from observer import Observer

class EmailService(Observer):
    def update(self, event_type, data):
        if event_type == "OrderPlaced":
            message = f"Your order {data['order_id']} has been placed!"
            self.send_email(data["customer_email"], message)
        elif event_type == "OrderShipped":
            message = f"Your order {data['order_id']} has been shipped! Tracking number: {data['tracking_number']}"
            self.send_email(data["customer_email"], message)

    def send_email(self, recipient, message):
        os.makedirs("output", exist_ok=True)
        log_message = f"Email sent to {recipient}: {message}"
        with open("output/emails.txt", "a") as file:
            file.write(log_message + "\n")
        print(f"EmailService: {log_message}")
