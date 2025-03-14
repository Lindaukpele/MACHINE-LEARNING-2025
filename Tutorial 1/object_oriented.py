class Car:
    country_of_origin = USA
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        #using double underscore to protect a variable, it makes the value protected and doesnt change

    def description(self):   #description is not a function, it is what the class can do
        print(f"This is a {self.make} {self.model} {self.color}")

my_car1 = Car("Toyota", "Corolla", "Black")
my_car1.description()
my_car1.display_info()
print(my_car1)

#Make a new object of Class Car - Hyundai, Sonata, Grey
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def description(self):
        print(f"This is a {self.make} {self.model} {self.color}")
    
    
    my_car2 = Car("Hyundai", "Sonata", "Black")
    my_car2.description()


#Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, color, battery_capacity):  #we can add more attributesthat was not in the parent class e.g battery_capacity
        super().__init__(make, model, color)
        self.battery_capacity = battery_capacity
    
    def display_battery(self):
        print(f"This electric car has a battery capacity: {self.battery_capacity}")

electric_car1 = ElectricCar("Tesla", "Model S", "Purple", 100)
electric_car1.description()
electric_car1.display_battery()

#Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}  barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
    
dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())





