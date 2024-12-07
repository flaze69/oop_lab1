from driver_module import *
from track_module import *
from car_module import *


class RaceManager:
    def __init__(self, cars, track):
        self.cars = cars
        self.track = track
        self.results = {}

    def start_race(self):
        print("Race Started!")
        self.track.road_map.display_map()
        for car in self.cars:
            if not car.driver:
                print(f"Car with engine power {car.engine_power} has no driver assigned!")
                continue
            self.results[car] = 0
            self.run_race(car)

    def run_race(self, car):
        total_time = 0
        for segment in self.track.segments:
            segment_speed = self.track.calculate_segment_speed(car, segment, car.driver)
            total_time += segment.length / segment_speed
        self.results[car] = total_time
        print(f"Car with engine power {car.engine_power} finished in {total_time:.2f} seconds")

    def display_results(self):
        print("\nRace Results:")
        for car, time in self.results.items():
            print(f"Car with engine power {car.engine_power}: {time:.2f} seconds")
            car.driver.license.display_license_info()

    def display_rating(self):
        print("\nRating:")
        for car in self.cars:
            print(f"Car with engine power {car.engine_power}: {car.calculate_rating()} rating")


# --- Тестування ---
driver1 = AggressiveDriver(aggression=10, error_chance=0.1, license_number="A123456", category="B")
driver2 = DefensiveDriver(aggression=4, error_chance=0.02, license_number="D654321", category="A")
driver3= BalancedDriver(aggression=6, error_chance=0.05, license_number="B789101", category="C")

car1 = SportsCar(engine_power=700, downforce=0.5, tire_wear=0.3, turbo_boost_capacity=20, turbo_boost=50)
car2 = SUVCar(engine_power=400, downforce=0.7, tire_wear=0.6, ground_clearance=20, off_road_mode=30)
car3 = ElectricCar(engine_power=300, downforce=0.4, tire_wear=0.2, battery_capacity=80, charging_speed=20)

car1.assign_driver(driver1)
car2.assign_driver(driver2)
car3.assign_driver(driver3)

segments = [
    TrackSegment("straight", 2000),
    TrackSegment("fast_turn", 800),
    TrackSegment("slow_turn", 400)
]

track = Track(segments)

race_manager = RaceManager(cars=[car1, car2, car3], track=track)

race_manager.start_race()
race_manager.display_results()
race_manager.display_rating()