from observer import Observer

class Subject:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def unregister_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify_observers(self, stock: str, price: float):
        for observer in self._observers:
            observer.update(stock, price)

class StockPriceService(Subject):
    def __init__(self):
        super().__init__()
        self.stock_prices = {}
    
    def update_stock_price(self, stock: str, price: float):
        old_price = self.stock_prices.get(stock, None)
        self.stock_prices[stock] = price
        
        if old_price is None or abs(price - old_price) / old_price >= 0.05:
            self.notify_observers(stock, price)
