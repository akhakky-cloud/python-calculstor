class Dog:
    def identify(self):
        print("Dog: Woof! 🐶")

class Cat:
    def identify(self):
        print("Cat: Meow! 🐱")

# Create objects
dog = Dog()
cat = Cat()

# Call the same method name on different objects
dog.identify()
cat.identify()