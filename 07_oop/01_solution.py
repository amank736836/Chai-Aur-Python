class Car:
    total_car = 0
    # brand = None
    # model = None

    # def __init__(self, brand, model):
    #     self.__brand = brand
    #     self.model = model

    def __init__(self, brand=None, model=None):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand + " !"

    def set_brand(self, brand):
        self.__brand = brand
        return f"Brand has been updated to {self.__brand}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "This is a car."

    @staticmethod
    def brief_description(self):
        return f"{self.full_name()} is a car."

    @property
    def model(self):
        return self.__model


# print("--------------------")


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        full_name = super().full_name()
        return f"{full_name} with battery size {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


# my_car = Car()
print("--------------------")

my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())
print(my_car.total_car)

print("--------------------")

print(my_car.set_brand("Suzuki"))
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())
print(my_car.total_car)

print("--------------------")

my_new_car = Car("Honda")
print(my_new_car.get_brand())
print(my_new_car.model)
print(my_new_car.full_name())
print(my_new_car.fuel_type())
print(my_new_car.total_car)

print("--------------------")

my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.get_brand())
print(my_electric_car.model)
print(my_electric_car.battery_size)
print(my_electric_car.full_name())
print(my_electric_car.fuel_type())
print(my_electric_car.total_car)

print("--------------------")

print(Car.total_car)
print(Car.brief_description(my_car))
print(Car.brief_description(my_new_car))
print(Car.brief_description(my_electric_car))

print("--------------------")

print(Car.general_description())

print("--------------------")

print(my_car.model)

print("--------------------")

print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))

print("--------------------")

print(issubclass(ElectricCar, Car))
print(issubclass(Car, ElectricCar))

print("--------------------")

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))

print("--------------------")


class Battery:
    def battery_info(self):
        return f"This car has a battery of {self.battery_size} kWh."


class Engine:
    def engine_info(self):
        return "This car has an engine."


class ElectricCarTwo(Battery, Engine, ElectricCar):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, battery_size)
        self.battery_size = battery_size


my_new_electric_car = ElectricCarTwo("Tesla", "Model S", 100)
print(my_new_electric_car.get_brand())
print(my_new_electric_car.model)
print(my_new_electric_car.battery_size)
print(my_new_electric_car.full_name())
print(my_new_electric_car.fuel_type())
print(my_new_electric_car.total_car)
print(my_new_electric_car.battery_info())
print(my_new_electric_car.engine_info())
