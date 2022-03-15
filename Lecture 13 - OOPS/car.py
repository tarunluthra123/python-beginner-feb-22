class Car:
    model = "Hatchback"
    color = "Black"
    price = 100000

    def __init__(self, m, c, p):
        self.model = m
        self.color = c
        self.price = p

    def drive(self):
        print("Zoom zoom zoom")

    def lock(self):
        print("Car is now locked")

    def unlock(self):
        print("Car is now unlocked")

    def printDetails(self, a, b, someValue):
        print("Model: ", self.model)
        print("Color: ", self.color)
        print("Price: ", self.price)
        print(a, b, someValue)


# Main part of the program
c1 = Car("Sedan", "Red", 200000)
# c2 = Car()

# c1.price = 20
# c1.model = "Sedan"
# c1.color = "Blue"

c1.printDetails(5, 3.2, "Hello")
# c2.printDetails(0, 0, 0)


# print(c1.color)  # Black
# print(c1.model)  # Hatchback
# print(c1.price)  # 100000

# c2.color = "Red"
# print(c2.color)  # Red

# c2.fuel = "CNG"
# print(c2.fuel)  # CNG

# print(c1.fuel)  # Error


# c1.drive()
# c2.drive()

# c1.lock()
# c2.lock()

# c1.unlock()
# c2.unlock()
