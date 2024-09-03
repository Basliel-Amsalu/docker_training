from event_manager import EventManager
from email_service import EmailService
from logging_service import LoggingService
from analytics_service import AnalyticsService

if __name__ == "__main__":
    event_manager = EventManager()

    email_service = EmailService()
    logging_service = LoggingService()
    analytics_service = AnalyticsService()

    # Register observers for specific events
    event_manager.register_observer("OrderPlaced", email_service)
    event_manager.register_observer("OrderPlaced", logging_service)
    event_manager.register_observer("OrderPlaced", analytics_service)

    event_manager.register_observer("OrderShipped", email_service)
    event_manager.register_observer("OrderShipped", logging_service)
    event_manager.register_observer("OrderShipped", analytics_service)

    # Simulate events
    event_manager.create_event("OrderPlaced", {
        "order_id": 123, 
        "customer_email": "customer@example.com", 
        "customer_id": 456
    })
    
    event_manager.create_event("OrderShipped", {
        "order_id": 123, 
        "tracking_number": "ABC123", 
        "customer_email": "customer@example.com"
    })
