class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

dog1 = Dog()
dog1.walk()
dog1.bark()
