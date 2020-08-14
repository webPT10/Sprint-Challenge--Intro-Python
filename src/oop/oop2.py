class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return 'vroooom'


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(num_wheels=2)

    def drive(self):
        return "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
# TODO
for v in vehicles:
    print(v.drive())