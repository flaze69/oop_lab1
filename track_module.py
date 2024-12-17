class Track:
    def __init__(self, segments):
        self.segments = segments
        self.length = sum(segment.length for segment in segments)
        self.total_turns = sum(1 for segment in segments if segment.segment_type in ["fast_turn", "slow_turn"])
        self.road_map = RoadMap(segments)

    def calculate_segment_speed(self, car, segment, driver):
        segment_modifier = segment.get_speed_modifier()
        driver_modifier = 1.0 - driver.error_chance
        speed = (car.engine_power * 0.05 * car.downforce * car.tire_wear * 
                 segment_modifier * driver_modifier * driver.aggression)
        return speed


class RoadMap:
    def __init__(self, segments):
        self.segments_info = self.generate_road_map(segments)

    def generate_road_map(self, segments):
        info = []
        for i, segment in enumerate(segments, start=1):
            info.append(f"Segment {i}: {segment.segment_type}, {segment.length} meters")
        return info

    def display_map(self):
        print("Road Map:")
        for segment_info in self.segments_info:
            print(segment_info)


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