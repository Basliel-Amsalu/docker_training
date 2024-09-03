from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event_type, data):
        pass

class Subject:
    def __init__(self):
        self._observers = {}

    def register_observer(self, event_type, observer):
        if event_type not in self._observers:
            self._observers[event_type] = []
        self._observers[event_type].append(observer)

    def unregister_observer(self, event_type, observer):
        if event_type in self._observers:
            self._observers[event_type].remove(observer)
            if not self._observers[event_type]:
                del self._observers[event_type]

    def notify_observers(self, event_type, data):
        if event_type in self._observers:
            for observer in self._observers[event_type]:
                observer.update(event_type, data)
