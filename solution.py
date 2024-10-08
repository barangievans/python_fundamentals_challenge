class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

# Test the Car class
if __name__ == "__main__":
    # Create instances of the Car class with different data
    cars = [
        Car("Toyota", "Corolla", 2020),
        Car("Honda", "Civic", 2018),
        Car("Ford", "Mustang", 2021),
        Car("Chevrolet", "Malibu", 2015),
        Car("Tesla", "Model S", 2022)
    ]

    # Display information for each car
    for car in cars:
        car.display_info()
