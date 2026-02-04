#Abstraction :- Hiding internal details & showing only essential features
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Dog(Animal):
    def make_sound(self):
        print("bho bho")


dog = Dog()
lion = Lion()

lion.make_sound()
dog.make_sound()
