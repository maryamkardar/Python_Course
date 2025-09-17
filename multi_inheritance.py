class Mammal:
    def has_fur(self):
        return True


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal, Mammal):
    def speak(self):
        return f'{self.name} says woof'

class Cat(Mammal, Animal):
    '''I am a cat'''
    def speak(self):
        return f'{self.name} says meow'

dog = Dog('Puppy')
cat = Cat('Whisy')

print(dog.speak())
print(dog.has_fur())
print(cat.speak())
print(cat.has_fur())
print(Cat.__doc__)

