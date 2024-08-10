class Transport:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def GetInfo(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}"

    def SetBrand(self, brand):
        self.brand = brand

    def SetModel(self, model):
        self.model = model

    def SetColor(self, color):
        self.color = color

class Car(Transport):
    def __init__(self, brand, model, color, speed, seat_count, manufacture_date):
        super().__init__(brand, model, color)
        self.speed = speed
        self.seat_count = seat_count
        self.manufacture_date = manufacture_date

    def GetInfo(self):
        base_info = super().GetInfo()
        return f"{base_info}, Speed: {self.speed}, Seat Count: {self.seat_count}, Manufacture Date: {self.manufacture_date}"

    def SetSpeed(self, speed):
        self.speed = speed

    def SetSeatCount(self, seat_count):
        self.seat_count = seat_count

    def SetManifactureDate(self, manufacture_date):
        self.manufacture_date = manufacture_date

class Truck(Transport):
    def __init__(self, brand, model, color, weight_capacity):
        super().__init__(brand, model, color)
        self.weight_capacity = weight_capacity

    def GetInfo(self):
        base_info = super().GetInfo()
        return f"{base_info}, Weight Capacity: {self.weight_capacity} tons"

    def SetWeightCapacity(self, weight_capacity):
        self.weight_capacity = weight_capacity


car = Car("Toyota", "Camry", "Red", 220, 5, "2022.01.15")
truck = Truck("Ford", "F-150", "Blue", 10)

print(car.GetInfo())
print(truck.GetInfo())

car.SetSpeed(240)
car.SetSeatCount(4)
car.SetManifactureDate("2023.02.20")

truck.SetWeightCapacity(15)

print(car.GetInfo())
print(truck.GetInfo())
