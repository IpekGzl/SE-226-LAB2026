class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"{self.vid} - {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= (n + 1)

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, mtype):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.mtype = mtype

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.mtype}"

def save_fleet_to_file(vehicles, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for v in vehicles:
            if isinstance(v, Car):
                file.write(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n")
            elif isinstance(v, Truck):
                file.write(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n")
            elif isinstance(v, Motorcycle):
                file.write(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.mtype}\n")

def load_fleet_from_file(filename):
    vehicles = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(",")

            if parts[0] == "Car":
                v = Car(parts[1], parts[2], parts[3], parts[4], parts[5])

            elif parts[0] == "Truck":
                v = Truck(parts[1], parts[2], parts[3], parts[4], parts[5])

            elif parts[0] == "Motorcycle":
                v = Motorcycle(parts[1], parts[2], parts[3], parts[4], parts[5])

            vehicles.append(v)

    return vehicles

vehicles = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]

save_fleet_to_file(vehicles, "fleet.txt")
loaded = load_fleet_from_file("fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
print(f" {len(loaded)} vehicles loaded successfully.")

print(" --- All Vehicles ---")
for v in loaded:
    print(v)

print(" --- Recent Vehicles (Last 4 Years) ---")
for v in loaded:
    if v.is_new(4):
        print(v)

print(" --- Electric Cars Only ---")
for v in loaded:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)
