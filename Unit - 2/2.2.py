class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")

class Bird(Animal):
    def make_sound(self):
        print("Chirp Chirp")

# Example
dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()
