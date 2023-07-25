from flask import Flask, render_template, request
import json

app = Flask(__name__)

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
                    result.append({
                        "source": source,
                        "departure": timing[str(source_station_index)],
                        "destination": destination,
                        "arrival": timing[str(destination_station_index)]
                    })
            return result
    
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    stations = [
        "SEALDAH (SDHM)",
        "PHOOL BAGAN (PBGB)",
        "SALT LAKE STADIUM (SSSA)",
        "BENGAL CHEMICAL (BCSD)",
        "CITY CENTER (CCSC)",
        "CENTRAL PARK (CPSA)",
        "KARUNA MOYEE (KESA)",
        "SALT LAKE SECTOR V (SVSA)"
    ]

    if request.method == 'POST':
        source_station = request.form['source_station']
        destination_station = request.form['destination_station']
        direction = request.form['direction']

        result = find_train_timings(source_station, destination_station, direction)

    return render_template('index.html', result=result, stations=stations)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
