import random
from driver_module import *
from track_module import *
from car_module import *


class RaceManager:
    def __init__(self, cars, track):
        self.cars = cars
        self.track = track
        self.results = {}

    def race_event(self, car):
        if random.randint(1, 10) <= car.driver.aggression:
            if random.random() >= car.driver.error_chance:
                return -1
            else: 
                return 1

        return 0

    def start_race(self):
        print("Race Started!")
        self.track.road_map.display_map()

        last_place_count = {car: 0 for car in self.cars}
        first_place_count = {car: 0 for car in self.cars}

        for car in self.cars:
            if not car.driver:
                print(f"Car with engine power {car.engine_power} has no driver assigned!")
                continue
            self.results[car] = 0
        
        for x in range(1, 21):
            print(f"Circle #{x}:")
            for car in self.cars:
                self.run_circle(car, x)

            sorted_results = sorted(self.results.items(), key=lambda item: item[1])
            ranked_cars = [car for car, _ in sorted_results]
            
            for i, car in enumerate(ranked_cars):
                if i == 0:
                    first_place_count[car] += 1
                    last_place_count[car] = 0
                    if first_place_count[car] >= 10:
                        car.driver.set_aggression_state(DefensiveState())
                elif i == 2:  # Останнє місце
                    last_place_count[car] += 1
                    first_place_count[car] = 0
                    if last_place_count[car] >= 5:
                        car.driver.set_aggression_state(AggressiveState())
                else:
                    last_place_count[car] = 0
                    first_place_count[car] = 0

            print()
            self.display_fatigue(x)

    def run_circle(self, car, circle):
        total_time = 0

        for segment in self.track.segments:
            if segment.segment_type == "fast_turn":
                state_modifier = car.driver.aggression_state.handle_fast_turn(car.driver)
            elif segment.segment_type == "slow_turn":
                state_modifier = car.driver.aggression_state.handle_slow_turn(car.driver)
            elif segment.segment_type == "straight":
                state_modifier = car.driver.aggression_state.handle_straight(car.driver)

            segment_speed = self.track.calculate_segment_speed(car, segment, car.driver)
            segment_time = segment.length / segment_speed

            segment_time += self.race_event(car) * state_modifier
            total_time += segment_time

        car.tire_wear -= 0.01

        total_time += total_time*((lambda f: 1 if f < 50 else 1.1 if f < 80 else 1.25 if f < 95 else 1.5)(car.driver.calculate_fatigue(self.track, circle)))

        self.results[car] += total_time
        print(f"{car.team} finished in {total_time:.2f} seconds")

    def display_results(self):
        print("\nRace Results:")
        for car, time in self.results.items():
            print(f"{car.team} team: {time:.2f} seconds")

    def display_rating(self):
        print("\nRating:")
        for car in self.cars:
            print(f"{car.team}: {car.calculate_rating():.2f} rating")
    
    def display_fatigue(self, circle):
        print("Drivers fatigue:")
        for car in self.cars:
            print(f"{car.team}: {car.driver.calculate_fatigue(self.track, circle):.2f}% driver fatigue")
        print()

# --- Тестування ---
driver1 = PofessionalDriver(aggression=9, error_chance=0.50, stamina=80, license_number="A123456", category="B", risk_factor=1.5)
driver2 = AmateurDriver(aggression=3, error_chance=0.05, stamina=100, license_number="D654321", category="A", focus=8)
driver3 = RookieDriver(aggression=7, error_chance=0.40, stamina=90, license_number="B789101", category="C", adaptability=6)

driver1.set_aggression_state(BalanceState())
driver2.set_aggression_state(BalanceState())
driver3.set_aggression_state(BalanceState())

car1 = SportsCar("Nissan", engine_power=700, downforce=0.2, tire_wear=1, turbo_boost_capacity=20, turbo_boost=50)
car2 = SUVCar("Toyota", engine_power=400, downforce=0.55, tire_wear=1, ground_clearance=20, off_road_mode=30)
car3 = ElectricCar("Mazda", engine_power=600, downforce=0.25, tire_wear=1, battery_capacity=80, charging_speed=20)

car1.assign_driver(driver1)
car2.assign_driver(driver2)
car3.assign_driver(driver3)

segments = [
    TrackSegment("straight", 2000),
    TrackSegment("fast_turn", 800),
    TrackSegment("slow_turn", 400),
    TrackSegment("straight", 1000),
    TrackSegment("fast_turn", 700),
    TrackSegment("slow_turn", 500)
]

track = Track(segments=segments)

race_manager = RaceManager(cars=[car1, car2, car3], track=track)

race_manager.start_race()
race_manager.display_results()