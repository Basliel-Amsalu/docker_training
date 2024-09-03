from stock_price_service import StockPriceService
from logging_service import LoggingService
from user_notification_service import UserNotificationService

def main():
    stock_service = StockPriceService()
    
    logging_service = LoggingService()
    user_notification_service = UserNotificationService(
        from_email="no-reply@example.com",
        to_email="user@example.com"
    )
    
    stock_service.register_observer(logging_service)
    stock_service.register_observer(user_notification_service)
    
    stock_service.update_stock_price("AAPL", 150)
    stock_service.update_stock_price("AAPL", 160)
    stock_service.update_stock_price("GOOGL", 2700)
    stock_service.update_stock_price("GOOGL", 2800)

if __name__ == "__main__":
    main()
