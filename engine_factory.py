from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, current_milage, last_service_mileage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_mileage

    def needs_service(self):
        return self.current_milage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, current_milage, last_service_mileage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_mileage

    def needs_service(self):
        return self.current_milage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False