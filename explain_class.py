class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Using the methods of the Dog class
print(my_dog.bark())  # Output: Buddy says woof!
print(f"My dog is {my_dog.get_age()} years old.")  # Output: My dog is 3 years old.