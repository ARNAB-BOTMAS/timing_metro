import json

def find_train_timings(source, destination, direction):
    with open('timetable.json') as f:
        data = json.load(f)
    
    direction_data = data.get(direction)
    if direction_data:
        source_station_index = None
        destination_station_index = None
        
        for index, station_name in direction_data['station'].items():
            if station_name == source:
                source_station_index = int(index)
            elif station_name == destination:
                destination_station_index = int(index)
        
        if source_station_index is not None and destination_station_index is not None:
            train_timings = direction_data['timing']
            result = []
            for timing in train_timings:
                if source_station_index < len(timing) and destination_station_index < len(timing):
                    result.append(f"Train from {source} at {timing[str(source_station_index)]} to {destination} at {timing[str(destination_station_index)]}")
            return result
    
    return None

source_station = input("Enter the source station: ")
destination_station = input("Enter the destination station: ")
direction = input("Enter the destination location up or down: ")

result = find_train_timings(source_station, destination_station, direction)
if result:
    for train_timing in result:
        print(train_timing)
else:
    print("No trains found for the specified source and destination in the given direction.")
