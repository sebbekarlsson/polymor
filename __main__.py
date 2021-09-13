import abc
import time


class Food(object):
    pass


class Animal(abc.ABC):

    def __init__(self):
        self.x = 0
        self.y = 0

    @abc.abstractmethod
    def eat(self, food: Food):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass

    @abc.abstractmethod
    def move(self, x, y):
        pass


class Monkey(Animal):

    def __init__(self, *args, **kwargs):
        Animal.__init__(self, *args, **kwargs)

    def eat(self, food: Food):
        print("Dont like food")


    def sleep(self):
        print("Sleeping...")
        time.sleep(5)
        print("Done sleeping.")

    def move(self, x, y):
        self.x += x
        self.y += y



class Human(Monkey):

    def __init__(self, name, *args, **kwargs):
        Monkey.__init__(self, *args, **kwargs)
        self.name = name


    def eat(self, food: Food):
        print("MMmm! I love it.")

    def speak(self):
        print(f"Hi my name is {self.name}")


class Kid(Human):


    def __init__(self, *args, **kwargs):
        Human.__init__(self, *args, **kwargs)


    def speak(self):
        print("Hej!")


kid = Kid("Sarah Doe")
kid.speak()

human = Human("John Doe")
monkey = Monkey()


print(isinstance(monkey, Animal))



def breed(animal1: Animal, animal2: Animal):
    pass
