class Car:
    def __init__(self, engine_power, downforce, tire_wear, driver=None):
        self.engine_power = engine_power
        self.downforce = downforce
        self.tire_wear = tire_wear
        self.driver = driver

    def assign_driver(self, driver):
        self.driver = driver


class SportsCar(Car):
    def __init__(self, engine_power, downforce, tire_wear, turbo_boost_capacity, turbo_boost, driver=None):
        super().__init__(engine_power, downforce, tire_wear, driver)
        self.turbo_boost_capacity = turbo_boost_capacity
        self.turbo_boost = turbo_boost

    def calculate_rating(self):
        return (self.engine_power * self.turbo_boost_capacity * self.downforce * 10) / self.tire_wear + self.turbo_boost


class SUVCar(Car):
    def __init__(self, engine_power, downforce, tire_wear, ground_clearance, off_road_mode, driver=None):
        super().__init__(engine_power, downforce, tire_wear, driver)
        self.ground_clearance = ground_clearance
        self.off_road_mode = off_road_mode

    def calculate_rating(self):
        return (self.engine_power * self.downforce * 8) / (self.tire_wear + self.ground_clearance / 100) + self.off_road_mode


class ElectricCar(Car):
    def __init__(self, engine_power, downforce, tire_wear, battery_capacity, charging_speed, driver=None):
        super().__init__(engine_power, downforce, tire_wear, driver)
        self.battery_capacity = battery_capacity
        self.charging_speed = charging_speed

    def calculate_rating(self):
        return (self.engine_power * self.downforce * 5) + (self.battery_capacity / 10) + self.charging_speed