import json
import re


class EasyRide:
    def __init__(self):
        self.database = None

    def input_data(self):
        self.database = json.loads(input("input:"))

    def check_type(self):
        error = {"total": 0, "bus_id": 0, "stop_id": 0,
                 "stop_name": 0, "next_stop": 0,
                 "stop_type": 0, "a_time": 0}
        for item in self.database:
            if type(item["bus_id"]) != int:
                error["total"] += 1
                error["bus_id"] += 1
            if type(item["stop_id"]) != int:
                error["total"] += 1
                error["stop_id"] += 1
            if type(item["stop_name"]) != str or not re.match(r'[A-Z][\w\s]* (Road|Avenue|Boulevard|Street)$', item["stop_name"], flags=re.A):
                error["total"] += 1
                error["stop_name"] += 1
            if type(item["next_stop"]) != int:
                error["total"] += 1
                error["next_stop"] += 1
            if item["stop_type"] not in ("O", "S", "F", ""):
                error["total"] += 1
                error["stop_type"] += 1
            if type(item["a_time"]) != str or not re.match(r"[01]\d:[012345]\d$", item["a_time"]):
                error["total"] += 1
                error["a_time"] += 1
        print(f'''Type and required field validation: {error["total"]} errors
stop_name: {error["stop_name"]}
stop_type: {error["stop_type"]}
a_time: {error["a_time"]}''')
        return error

    def count_stops(self):
        bus_stops = {}
        for item in self.database:
            bus_stops.setdefault(item["bus_id"], 0)
            bus_stops[item["bus_id"]] += 1
        for bus_id in bus_stops:
            print(f'bus_id: {bus_id}, stops: {bus_stops[bus_id]}')


bus = EasyRide()
bus.input_data()
bus.count_stops()

