class Track:
    def __init__(self, segments):
        self.segments = segments

    def calculate_segment_speed(self, car, segment, driver):
        segment_modifier = segment.get_speed_modifier()
        driver_modifier = 1.0 - driver.error_chance
        speed = car.engine_power * 0.2 * car.downforce * car.tire_wear * segment_modifier * driver_modifier * driver.aggression
        return speed


class TrackSegment:
    def __init__(self, segment_type, length):
        self.segment_type = segment_type
        self.length = length

    def get_speed_modifier(self):
        if self.segment_type == "straight":
            return 1.2
        elif self.segment_type == "fast_turn":
            return 0.9
        elif self.segment_type == "slow_turn":
            return 0.7


class Car:
    def __init__(self, engine_power, downforce, tire_wear):
        self.engine_power = engine_power
        self.downforce = downforce
        self.tire_wear = tire_wear

    def adjust_parameters(self, downforce, tire_wear):
        self.downforce = downforce
        self.tire_wear = tire_wear


class Driver:
    def __init__(self, aggression, error_chance):
        self.aggression = aggression
        self.error_chance = error_chance


class RaceManager:
    def __init__(self, cars, drivers, track):
        self.cars = cars
        self.drivers = drivers
        self.track = track
        self.results = {}

    def start_race(self):
        print("Race Started!")
        for car, driver in zip(self.cars, self.drivers):
            self.results[car] = 0  # Початковий час кожної машини
            self.run_race(car, driver)

    def run_race(self, car, driver):
        total_time = 0
        for segment in self.track.segments:
            segment_speed = self.track.calculate_segment_speed(car, segment, driver)
            total_time += segment.length / segment_speed
        self.results[car] = total_time
        print(f"Car with engine power {car.engine_power} finished in {total_time:.2f} seconds")

    def display_results(self):
        print("\nRace Results:")
        for car, time in self.results.items():
            print(f"Car with engine power {car.engine_power}: {time:.2f} seconds")

# --- Тестування ---

driver1 = Driver(aggression=8, error_chance=0.05)
driver2 = Driver(aggression=6, error_chance=0.08)

car1 = Car(engine_power=550, downforce=0.65, tire_wear=0.15)
car2 = Car(engine_power=600, downforce=0.7, tire_wear=0.20)

segments = [
    TrackSegment("straight", 2000),
    TrackSegment("fast_turn", 800),
    TrackSegment("slow_turn", 400)
]

track = Track(segments)

race_manager = RaceManager(cars=[car1, car2], drivers=[driver1, driver2], track=track)

race_manager.start_race()

race_manager.display_results()