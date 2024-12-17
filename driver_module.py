from abc import ABC, abstractmethod

class AggressionState(ABC):
    @abstractmethod
    def handle_fast_turn(self, driver):
        pass

    @abstractmethod
    def handle_slow_turn(self, driver):
        pass

    @abstractmethod
    def handle_straight(self, driver):
        pass


class BalanceState(AggressionState):
    def handle_fast_turn(self, driver):
        return driver.error_chance * 5

    def handle_slow_turn(self, driver):
        return driver.error_chance * 40

    def handle_straight(self, driver):
        return driver.error_chance * 10


class AggressiveState(AggressionState):
    def handle_fast_turn(self, driver):
        return driver.error_chance * 15

    def handle_slow_turn(self, driver):
        return driver.error_chance * 15

    def handle_straight(self, driver):
        return driver.error_chance * 20


class DefensiveState(AggressionState):
    def handle_fast_turn(self, driver):
        return driver.error_chance * 25

    def handle_slow_turn(self, driver):
        return driver.error_chance * 15

    def handle_straight(self, driver):
        return driver.error_chance * 30

class Driver(ABC):
    def __init__(self, aggression, error_chance, stamina, license_number, category):
        self.aggression = aggression
        self.error_chance = error_chance
        self.stamina = stamina
        self.aggression_state = BalanceState()
        self.license = DriverLicense(license_number, category)

    def set_aggression_state(self, state):
        self.aggression_state = state

    @abstractmethod
    def calculate_fatigue(self, track, circle):
        pass


class PofessionalDriver(Driver):
    def __init__(self, aggression, error_chance, stamina, license_number, category, risk_factor):
        super().__init__(aggression, error_chance, stamina, license_number, category)
        self.risk_factor = risk_factor
   
    def calculate_fatigue(self, track, circle):
        fatigue = (circle ** 2.3 * track.total_turns * self.risk_factor ** 2 + self.aggression * 100) / self.stamina
        return fatigue

class AmateurDriver(Driver):
    def __init__(self, aggression, error_chance, stamina, license_number, category, focus):
        super().__init__(aggression, error_chance, stamina, license_number, category)
        self.focus = focus

    def calculate_fatigue(self, track, circle):
        fatigue = (circle*track.length) / ((self.focus * self.stamina) + (circle ** 1.4 *track.total_turns))
        return fatigue


class RookieDriver(Driver):
    def __init__(self, aggression, error_chance, stamina, license_number, category, adaptability):
        super().__init__(aggression, error_chance, stamina, license_number, category)
        self.adaptability = adaptability

    def calculate_fatigue(self, track, circle):
        fatigue = ((circle*(track.length + circle**2) * (1 - self.adaptability / 10)) / self.stamina)/5
        return fatigue


class DriverLicense:
    def __init__(self, license_number, category):
        self.license_number = license_number
        self.category = category

    def display_license_info(self):
        print(f"License Number: {self.license_number}, Category: {self.category}")