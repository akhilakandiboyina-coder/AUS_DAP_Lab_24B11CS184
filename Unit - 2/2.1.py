class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.make + " " + self.model + " is starting...")

    def stop(self):
        print(self.make + " " + self.model + " is stopping...")

# Example
my_car = Car("Toyota", "Camry", 2022)
my_car.start()
my_car.stop()
