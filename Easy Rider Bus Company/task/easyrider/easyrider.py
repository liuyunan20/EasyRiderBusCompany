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
            if type(item["stop_name"]) != str or not item["stop_name"]:
                error["total"] += 1
                error["stop_name"] += 1
            if type(item["next_stop"]) != int:
                error["total"] += 1
                error["next_stop"] += 1
            if item["stop_type"] not in ("O", "S", "F", ""):
                error["total"] += 1
                error["stop_type"] += 1
            if type(item["a_time"]) != str or not re.match(r"..:..", item["a_time"]):
                error["total"] += 1
                error["a_time"] += 1
        print(f'''Type and required field validation: {error["total"]} errors
bus_id: {error["bus_id"]}
stop_id: {error["stop_id"]}
stop_name: {error["stop_name"]}
next_stop: {error["next_stop"]}
stop_type: {error["stop_type"]}
a_time: {error["a_time"]}''')
        return error


bus = EasyRide()
bus.input_data()
type_error = bus.check_type()

