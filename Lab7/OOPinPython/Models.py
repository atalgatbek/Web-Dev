class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        return "Some generic sound"

    def info(self):
        return f"{self.name} is  {self.age} years old, and weights {self.weight} kg"

    def __str__(self):
        return f"Name:{self.name} Age,{self.age}, Weight: {self.weight} "





class Dog(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(self, name, age, weight)
        self.breed = breed
    def speak(self):
        return "Woof!"
    def eat(self):
        return f"{self.name} eats meat"
    def __str__(self):
        return f"Name: {self.name}, Breed: {self.breed}"




class Cat(Animal):
    def __init__(self,name, age, weight, color):
        super().__init__(self,age,name,weight)
        self.color=color
    def speak(self):
        return"Meow!"
    def play(self):
        return f"{self.name} plays with ball!"
    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"
