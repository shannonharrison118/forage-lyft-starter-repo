import unittest
from datetime import datetime

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from battery import spindler_battery
from battery import nubbin_battery
from car_factory import CarFactory
import engine
import battery


class TestBattery(unittest.TestCase):
    def test_SpindlerBattery(self):
        spindler = spindler_battery.SpindlerBattery(datetime(2014,11,11).date())
        self.assertTrue(spindler.needs_service())

    def test_NubbinBattery(self):
        nubbin = nubbin_battery.NubbinBattery(datetime(2016,11,11).date())
        self.assertTrue(nubbin.needs_service())

class TestEngine(unittest.TestCase):
    def test_CapuletEngine(self):
        capulet = capulet_engine.CapuletEngine(55000, 25000)
        self.assertTrue(capulet.needs_service())

    def test_SternmanEngine(self):
        sternman = sternman_engine.SternmanEngine(True)
        self.assertTrue(sternman.needs_service())

    def test_WilloughbyEngine(self):
        willoughby = willoughby_engine.WilloughbyEngine(90000, 20000)
        self.assertTrue(willoughby.needs_service())

class TestCarModel(unittest.TestCase):
    def test_calliope(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.date-3)
        current_mileage = 0
        last_service_mileage = 0
        caliope = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(caliope.needs_service())

    def test_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.date-3)
        current_mileage = 0
        last_service_mileage = 0
        glissade = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.needs_service())

    def test_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.date-3)
        current_mileage = 0
        last_service_mileage = 0
        palindrome = CarFactory.create_palindrome(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(palindrome.needs_service())

    def test_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.date-5)
        current_mileage = 0
        last_service_mileage = 0
        rorschach = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(rorschach.needs_service())

    def test_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.date-5)
        current_mileage = 0
        last_service_mileage = 0
        thovex = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
