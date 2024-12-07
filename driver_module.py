from abc import ABC, abstractmethod


class Driver(ABC):
    def __init__(self, aggression, error_chance, license_number, category):
        self.aggression = aggression
        self.error_chance = error_chance
        self.license = DriverLicense(license_number, category)

    @abstractmethod
    def drive_style(self):
        pass


class AggressiveDriver(Driver):
    def __init__(self, aggression, error_chance, license_number, category):
        super().__init__(aggression, error_chance, license_number, category)

    def drive_style(self):
        return "Aggressive driving: Prioritizes speed and risk-taking."


class DefensiveDriver(Driver):
    def __init__(self, aggression, error_chance, license_number, category):
        super().__init__(aggression, error_chance, license_number, category)

    def drive_style(self):
        return "Defensive driving: Cautious, prioritizes safety over speed."


class BalancedDriver(Driver):
    def __init__(self, aggression, error_chance, license_number, category):
        super().__init__(aggression, error_chance, license_number, category)

    def drive_style(self):
        return "Balanced driving: Mix of speed and caution, adaptable to conditions."


class DriverLicense:
    def __init__(self, license_number, category):
        self.license_number = license_number
        self.category = category

    def display_license_info(self):
        print(f"License Number: {self.license_number}, Category: {self.category}")