from observer import Observer

class LoggingService(Observer):
    def __init__(self, log_file: str = 'stock_prices.log'):
        self.log_file = log_file
    
    def update(self, stock: str, price: float):
        message = f"LoggingService: Stock {stock} price updated to {price}\n"
        print(message)
        with open(self.log_file, 'a') as file:
            file.write(message)
