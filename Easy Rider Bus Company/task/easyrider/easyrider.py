import json
import re


class EasyRide:
    def __init__(self):
        self.database = None
        self.stops = {"S": set(), "F": set(), "T": set()}
        self.bus_sf_stops = {}
        self.bus_stops = {}
        self.stop_times = {}

    def input_data(self):
        self.database = json.loads(input("input:"))
        for item in self.database:
            if item["stop_type"] == "S" or item["stop_type"] == "F":
                # add start stops and final stops
                self.stops[item["stop_type"]].add(item["stop_name"])
                self.bus_sf_stops.setdefault(item["bus_id"], {"S": [], "F": []})
                self.bus_sf_stops[item["bus_id"]][item["stop_type"]].append(item["stop_name"])
            # find out transfer stops
            self.bus_stops.setdefault(item["bus_id"], set())
            self.bus_stops[item["bus_id"]].add(item["stop_name"])
        for value in self.bus_stops.values():
            for stop in value:
                self.stop_times.setdefault(stop, 0)
                self.stop_times[stop] += 1
        for stop in self.stop_times:
            if self.stop_times[stop] > 1:
                self.stops["T"].add(stop)

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
        for bus_id in self.bus_stops:
            print(f'bus_id: {bus_id}, stops: {len(self.bus_stops[bus_id])}')

    def start_trans_final(self):
        for line in self.bus_sf_stops:
            if len(self.bus_sf_stops[line]["S"]) != 1 or len(self.bus_sf_stops[line]["F"]) != 1:
                print(f"There is no start or end stop for the line: {line}.")
                return

        print(f'''Start stops: {len(self.stops["S"])} {sorted(list(self.stops["S"]))}
Transfer stops: {len(self.stops["T"])} {sorted(list(self.stops["T"]))}
Finish stops: {len(self.stops["F"])} {sorted(list(self.stops["F"]))}''')

    def check_a_time(self):
        bus_stop_time = {}
        stop_id_name = {}
        for item in self.database:
            stop_id_name[item["stop_id"]] = item["stop_name"]
            bus_stop_time.setdefault(item["bus_id"], {})
            bus_stop_time[item["bus_id"]][item["stop_id"]] = (item["a_time"], item["next_stop"])
        print("Arrival time test:")
        time_ok = True
        for bus_id in bus_stop_time:
            for stop in bus_stop_time[bus_id]:
                current_time = bus_stop_time[bus_id][stop][0].split(":")  # line[stop][0] is current a_time
                next_stop = bus_stop_time[bus_id][stop][1]
                if bus_stop_time[bus_id].get(next_stop):  # line[stop][1] is next stop id
                    next_time = bus_stop_time[bus_id][next_stop][0].split(":")
                    if int(next_time[0]) < int(current_time[0]) or (int(next_time[0]) == int(current_time[0]) and int(next_time[1]) < int(current_time[1])):
                        print(f"bus_id line {bus_id}: wrong time on station {stop_id_name[next_stop]}")
                        time_ok = False
                        break
                else:
                    continue
        if time_ok:
            print("OK")

    def check_on_demand(self):
        wrong_type_stops = []
        for term in self.database:
            if term["stop_type"] == "O" and (term["stop_name"] in self.stops["S"]|self.stops["T"]|self.stops["F"]):
                wrong_type_stops.append(term["stop_name"])
        print("On demand stops test:")
        if wrong_type_stops:
            print(f'Wrong stop type: {sorted(wrong_type_stops)}')
        else:
            print("OK")


bus = EasyRide()
bus.input_data()
bus.check_on_demand()

