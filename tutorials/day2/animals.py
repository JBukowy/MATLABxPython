class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Animal Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the initializer of the parent class
        super().__init__(name)
        self.breed = breed

    def display_info(self):
        # Override the display_info method of the parent class
        print(f"Dog Name: {self.name}, Breed: {self.breed}")

    def bark(self):
        print("Woof! Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        # Call the initializer of the parent class
        super().__init__(name)
        self.color = color

    def display_info(self):
        # Override the display_info method of the parent class
        print(f"Cat Name: {self.name}, Color: {self.color}")

class Bird(Animal):
    def __init__(self, name, species):
        # Call the initializer of the parent class
        super().__init__(name)
        self.species = species

    def display_info(self):
        # Call the display_info method of the parent class
        super().display_info()
        print(f"Species: {self.species}")

def main():
    kitty = Cat("Niky","Tortie")
    kitty.display_info()

if __name__ == "__main__":
    main()