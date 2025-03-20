class Car:
    def move(self):
        print("The car is moving fast")


class Bike:
    def move(self):
        print("The bike is moving slowly")


def make_it_move(vehicle):
    vehicle.move()


if __name__ == "__main__":
    my_car = Car()
    my_bike = Bike()

    print("Moving vehicles:")
    make_it_move(my_car)
    make_it_move(my_bike)
