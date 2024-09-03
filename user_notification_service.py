from observer import Observer

class UserNotificationService(Observer):
    def __init__(self, from_email: str, to_email: str):
        self.from_email = from_email
        self.to_email = to_email
    
    def update(self, stock: str, price: float):
        message = f"UserNotificationService: Notification sent for stock {stock} with price {price}\n"
        print(message)
        self.mock_send_email_notification(stock, price)
    
    def mock_send_email_notification(self, stock: str, price: float):
        print(f"[MOCK EMAIL] From: {self.from_email}")
        print(f"[MOCK EMAIL] To: {self.to_email}")
        print(f"[MOCK EMAIL] Subject: Stock Update: {stock}")
        print(f"[MOCK EMAIL] Body: The price for stock {stock} has changed to {price}.\n")
